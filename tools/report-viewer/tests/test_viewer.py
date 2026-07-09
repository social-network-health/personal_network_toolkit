"""Browser-render tests for the Visual Validator viewer (Playwright).

OPT-IN / not in `just ci`. Run:  just test-viewer   (one-time:  just setup-test)

These close the Phase-2 gap: they confirm the viewer actually *renders* a report
(not just that the JSON is valid — that's tools/report-fixtures-lint.py) in both the
developer (A0) and end-user (A1) registers, plus the side-by-side view. A broken
selector or a render regression turns them red. Tests pin the view via ?mode= so they
don't depend on the persisted default.
"""
from __future__ import annotations

import re

import pytest
from playwright.sync_api import Page, expect

# (sample file, expected posture, expected finding-card count, an ac_id that must render)
SAMPLES = [
    ("01-conformant-minimal-pna.json", "conformant", 7, "AC-MCP-A"),
    ("02-non-conformant-leaky-app.json", "non-conformant", 3, "AC-PRM-A"),
    ("03-mixed-exceptions-and-constraints.json", "mixed", 3, "AC-MCP-A"),
    ("04-not-pna-active-exception.json", "not-pna-active", 3, "AC-1"),
    ("05-adjacent-app-goal-impact.json", "not-a-pna", 3, "AC-1"),
]


def _attach_error_capture(page: Page) -> list[str]:
    """Collect uncaught JS errors + console errors (ignoring the favicon 404 noise)."""
    errs: list[str] = []

    def on_console(msg):
        if msg.type == "error" and "favicon" not in msg.text.lower():
            errs.append("console: " + msg.text)

    page.on("console", on_console)
    page.on("pageerror", lambda e: errs.append("pageerror: " + str(e)))
    return errs


# ---- developer (A0) register ----

@pytest.mark.parametrize("sample,posture,n_findings,ac_id", SAMPLES)
def test_developer_register_renders(page: Page, viewer_url, sample, posture, n_findings, ac_id):
    errs = _attach_error_capture(page)
    page.goto(f"{viewer_url}/index.html?report=sample-reports/{sample}&mode=developer", wait_until="networkidle")
    page.locator(".finding").first.wait_for(state="visible", timeout=5000)

    # posture badge = first badge in the summary card (2nd .card: header, then summary)
    expect(page.locator(".card").nth(1).locator(".badge").first).to_have_text(posture)

    # findings: the right number, including a known ac_id
    ac_texts = page.locator(".finding .ac").all_inner_texts()
    assert len(ac_texts) == n_findings, f"{sample}: {len(ac_texts)} findings, expected {n_findings} ({ac_texts})"
    assert ac_id in ac_texts, f"{sample}: missing a finding for {ac_id} in {ac_texts}"

    # candidate name flows into the document title
    expect(page).to_have_title(re.compile(r" — PNA evaluate-report$"))

    # developer mode only — no end-user cells leak in
    assert page.locator(".a1-finding").count() == 0

    assert not errs, f"{sample}: console/page errors: {errs}"


def test_evidence_source_badges_render(page: Page, viewer_url):
    """Sample 03 carries deterministic + llm + human evidence — all three badges must show."""
    page.goto(
        f"{viewer_url}/index.html?report=sample-reports/03-mixed-exceptions-and-constraints.json&mode=developer",
        wait_until="networkidle",
    )
    page.locator(".finding").first.wait_for(state="visible", timeout=5000)
    badges = " ".join(page.locator(".ev-src").all_inner_texts())
    for source in ("deterministic", "llm", "human"):
        assert source in badges, f"missing evidence-source badge {source!r} in {badges!r}"


# ---- end-user (A1) register ----

def test_end_user_register_renders(page: Page, viewer_url):
    """Sample 02 is non-conformant — the plain-language register shows 'At risk' + the caveat."""
    errs = _attach_error_capture(page)
    page.goto(
        f"{viewer_url}/index.html?report=sample-reports/02-non-conformant-leaky-app.json&mode=end-user",
        wait_until="networkidle",
    )
    page.locator(".a1-finding").first.wait_for(state="visible", timeout=5000)
    assert page.locator(".a1-finding").count() == 3
    # end-user mode only — no developer cards
    assert page.locator(".finding").count() == 0
    # the two non-conformant findings read "At risk"
    expect(page.locator(".a1-verdict", has_text="At risk").first).to_be_visible()
    # the liability-safe caveat is present
    expect(page.locator(".caveat").first).to_be_visible()
    assert not errs, f"end-user render errors: {errs}"


# ---- side-by-side (finding-aligned) ----

def test_side_by_side_shows_both_registers_aligned(page: Page, viewer_url):
    page.goto(
        f"{viewer_url}/index.html?report=sample-reports/03-mixed-exceptions-and-constraints.json&mode=side-by-side",
        wait_until="networkidle",
    )
    page.locator(".sxs").wait_for(state="visible", timeout=5000)
    # both registers present, one cell each per finding (aligned 2-col grid)
    assert page.locator(".a1-finding").count() == 3
    assert page.locator(".finding").count() == 3
    expect(page.locator(".caveat").first).to_be_visible()


# ---- the toggle re-renders without a reload ----

def test_mode_toggle_re_renders(page: Page, viewer_url):
    page.goto(
        f"{viewer_url}/index.html?report=sample-reports/01-conformant-minimal-pna.json&mode=developer",
        wait_until="networkidle",
    )
    page.locator(".finding").first.wait_for(state="visible", timeout=5000)
    assert page.locator(".finding").count() == 7 and page.locator(".a1-finding").count() == 0

    page.locator("[data-mode='end-user']").click()
    page.locator(".a1-finding").first.wait_for(state="visible", timeout=5000)
    assert page.locator(".a1-finding").count() == 7 and page.locator(".finding").count() == 0


# ---- edge cases ----

def test_empty_state(page: Page, viewer_url):
    page.goto(f"{viewer_url}/index.html", wait_until="networkidle")
    expect(page.locator(".empty")).to_be_visible()


def test_malformed_report_shows_error(page: Page, viewer_url):
    page.goto(f"{viewer_url}/index.html?report=tests/fixtures/broken.json", wait_until="networkidle")
    expect(page.locator(".error")).to_be_visible()


# ---- report-set flip-through (Phase 5) ----

def test_flip_through_a_set_via_reports_param(page: Page, viewer_url):
    files = [
        "01-conformant-minimal-pna.json",
        "02-non-conformant-leaky-app.json",
        "03-mixed-exceptions-and-constraints.json",
    ]
    reports = ",".join("sample-reports/" + f for f in files)
    page.goto(f"{viewer_url}/index.html?reports={reports}&mode=developer", wait_until="networkidle")
    page.locator(".navbar").wait_for(state="visible", timeout=5000)

    expect(page.locator(".navpos")).to_have_text("1 / 3")
    expect(page.locator(".cand-name")).to_contain_text("vault-cli")
    # the jump dropdown lists all three
    assert page.locator(".navselect option").count() == 3

    page.locator("button", has_text="Next").click()
    expect(page.locator(".navpos")).to_have_text("2 / 3")
    expect(page.locator(".cand-name")).to_contain_text("contacts-sync-pro")

    page.keyboard.press("ArrowRight")
    expect(page.locator(".navpos")).to_have_text("3 / 3")
    expect(page.locator(".cand-name")).to_contain_text("fellows_local_db")

    page.keyboard.press("ArrowLeft")
    expect(page.locator(".navpos")).to_have_text("2 / 3")

    # jump straight to the first via the dropdown
    page.locator(".navselect").select_option("0")
    expect(page.locator(".navpos")).to_have_text("1 / 3")


def test_flip_through_a_directory_manifest(page: Page, viewer_url):
    page.goto(f"{viewer_url}/index.html?dir=tests/fixtures/dirset&mode=developer", wait_until="networkidle")
    page.locator(".navbar").wait_for(state="visible", timeout=5000)
    expect(page.locator(".navpos")).to_have_text("1 / 2")
    expect(page.locator(".cand-name")).to_contain_text("App A")
    page.keyboard.press("ArrowRight")
    expect(page.locator(".navpos")).to_have_text("2 / 2")
    expect(page.locator(".cand-name")).to_contain_text("App B")


def test_mode_is_preserved_across_a_flip(page: Page, viewer_url):
    reports = ",".join("sample-reports/" + f for f in
                       ["02-non-conformant-leaky-app.json", "03-mixed-exceptions-and-constraints.json"])
    page.goto(f"{viewer_url}/index.html?reports={reports}&mode=side-by-side", wait_until="networkidle")
    page.locator(".sxs").wait_for(state="visible", timeout=5000)
    page.keyboard.press("ArrowRight")
    expect(page.locator(".navpos")).to_have_text("2 / 2")
    # still side-by-side after flipping
    expect(page.locator(".sxs")).to_be_visible()
    assert page.locator(".a1-finding").count() == page.locator(".finding").count()


def test_single_report_has_no_nav(page: Page, viewer_url):
    page.goto(f"{viewer_url}/index.html?report=sample-reports/01-conformant-minimal-pna.json&mode=developer",
              wait_until="networkidle")
    page.locator(".finding").first.wait_for(state="visible", timeout=5000)
    assert page.locator(".navbar").count() == 0


# ---- Mode-2 (goal-impact) rendering: schema 0.2 ----

def test_mode2_developer_renders_strip_and_classification(page: Page, viewer_url):
    """Sample 05 is a Mode-2 report: the classification banner and the per-Goal
    impact strip must render in the developer register."""
    errs = _attach_error_capture(page)
    page.goto(
        f"{viewer_url}/index.html?report=sample-reports/05-adjacent-app-goal-impact.json&mode=developer",
        wait_until="networkidle",
    )
    page.locator(".finding").first.wait_for(state="visible", timeout=5000)

    # classification banner in the candidate card
    expect(page.locator(".class-line")).to_contain_text("note-taking editor")
    # the verbatim user declaration that brought the app in scope
    expect(page.locator(".class-decl")).to_contain_text("just an editor")
    # mode + nexus chips
    chips = " ".join(page.locator(".card").first.locator(".chip").all_inner_texts())
    assert "goal-impact" in chips, f"mode chip missing in {chips!r}"
    assert "user-declared" in chips, f"nexus-source chip missing in {chips!r}"

    # per-Goal impact strip: exactly 4 tiles, in Goal order, with impact badges
    tiles = page.locator(".gi-tile")
    assert tiles.count() == 4
    expect(tiles.nth(0)).to_contain_text("Goal 1")
    expect(tiles.nth(0).locator(".badge")).to_have_text("protects")
    expect(tiles.nth(2).locator(".badge")).to_have_text("diminishes")
    # diminishes carries its grounding note
    expect(tiles.nth(2).locator(".gi-note")).to_contain_text("cloud sync")

    assert not errs, f"Mode-2 developer render errors: {errs}"


def test_mode2_end_user_verdict_is_goal_impact(page: Page, viewer_url):
    """In the end-user register the not-a-pna posture reads as a goal-impact
    verdict (never a pass/fail), and the strip renders there too."""
    page.goto(
        f"{viewer_url}/index.html?report=sample-reports/05-adjacent-app-goal-impact.json&mode=end-user",
        wait_until="networkidle",
    )
    page.locator(".a1-summary").wait_for(state="visible", timeout=5000)
    expect(page.locator(".a1-bigverdict")).to_contain_text("goal-impact read")
    assert page.locator(".gi-tile").count() == 4


def test_pre_02_reports_render_without_strip(page: Page, viewer_url):
    """A 0.1 report has no classification/goal_impacts — nothing new may render."""
    page.goto(
        f"{viewer_url}/index.html?report=sample-reports/01-conformant-minimal-pna.json&mode=developer",
        wait_until="networkidle",
    )
    page.locator(".finding").first.wait_for(state="visible", timeout=5000)
    assert page.locator(".gi-tile").count() == 0
    assert page.locator(".class-line").count() == 0


# ---- grouped picker: per-app run history ----

def test_picker_groups_runs_by_app(page: Page, viewer_url):
    """Two runs of App C + one App A: the dropdown groups under optgroups per app,
    run entries read 'date · posture', and jumping to a run renders it."""
    reports = ",".join([
        "tests/fixtures/runset/c2.json",
        "tests/fixtures/runset/c1.json",
        "tests/fixtures/dirset/a.json",
    ])
    page.goto(f"{viewer_url}/index.html?reports={reports}&mode=developer", wait_until="networkidle")
    page.locator(".navbar").wait_for(state="visible", timeout=5000)

    # grouped: one optgroup per app, App C holding both runs
    assert page.locator(".navselect optgroup").count() == 2
    appc = page.locator(".navselect optgroup[label='App C'] option")
    assert appc.count() == 2
    labels = appc.all_inner_texts()
    assert labels == ["2026-07-01 · conformant", "2026-06-01 · non-conformant"], labels

    # walk App C's history via the picker: run 1 is index 1 in the set
    page.locator(".navselect").select_option("1")
    expect(page.locator(".navpos")).to_have_text("2 / 3")
    expect(page.locator(".card").nth(1).locator(".badge").first).to_have_text("non-conformant")


def test_flat_set_labels_carry_app_and_posture(page: Page, viewer_url):
    """A set with all-distinct apps stays flat (no optgroups) but labels read
    'name · date · posture'."""
    reports = ",".join([
        "tests/fixtures/dirset/a.json",
        "tests/fixtures/dirset/b.json",
    ])
    page.goto(f"{viewer_url}/index.html?reports={reports}&mode=developer", wait_until="networkidle")
    page.locator(".navbar").wait_for(state="visible", timeout=5000)
    assert page.locator(".navselect optgroup").count() == 0
    labels = page.locator(".navselect option").all_inner_texts()
    assert all(" · " in lbl for lbl in labels), labels
    assert labels[0].startswith("App A"), labels
