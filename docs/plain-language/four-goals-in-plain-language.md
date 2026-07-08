# What Personal Network Applications promise you — in plain language

This toolkit helps people ensure that their apps protect their contact and relationship data by keeping several promises.

The link after each promise carries the **name** of the exact commitment in the
project's technical specification.  The name points
straight to the commitment.  Where a single promise covers more than one technical commitment, you'll see
more than one commitment name.

This toolkit can help you check that an application is keeping all of the promises below.  If an application does that, it's a Personal Network Application.

(If you want the full technical version with all the engineering detail, that
lives in the project's [specification](https://github.com/social-network-health/personal_network_toolkit/blob/main/spec/PNA_Spec.md). This page is the same set of promises, said
plainly.)

---

## 1. Your people stay on your own device

> **The app keeps a copy of your contacts and the private things you remember
> about people right on your own device, so they stay with you no matter what
> happens to any online account.**

- It keeps the everyday facts that came from elsewhere (names, emails) separate
  from the private things *you* add (your notes, who you'd call first), so the
  private side can be guarded more carefully. ([Sovereign, sealed private layer](../../spec/PNA_Spec.md#ac-1))
- Your device or web browser can't quietly take over your stored information or
  clear it out without you knowing. ([Service worker never owns SQLite](../../spec/axes.md#rz-4))
- Even if an online service ever locks you out, the copy on your device still
  opens and works. ([Stale session never locks users out of cached data](../../spec/PNA_Spec.md#ac-5))
- New contact information is pulled in only when you ask for it — the app never
  reaches back out to your accounts on its own in the background. ([Re-ingestion is always user-initiated](../../spec/PNA_Spec.md#ac-21))

---

## 2. You can check that it's telling the truth

> **You — or someone helping you — can look under the hood and confirm the app
> actually does what it promises, and that your contacts really came from where
> it says, instead of just having to trust it.**

- There's always a way to force the app open or reset it, even when it's frozen
  or stuck. ([Always-reachable diagnostic escape](../../spec/PNA_Spec.md#ac-6))
- The app comes with built-in tools for showing what it's doing and for reporting
  a problem, so trouble can be looked at directly instead of guessed at. ([Self-service field-debug substrate](../../spec/PNA_Spec.md#ac-7))
- Every copy of the app clearly shows which version it is, so you always know
  exactly what you're running. ([Build label tied to source revision, substituted at build and serve time](../../spec/PNA_Spec.md#ac-15))
- The app is honest about what it can and can't do on your particular device — it
  never claims a protection it can't actually deliver. ([Honest capability assessment](../../spec/PNA_Spec.md#ac-22))
- Every contact can be traced back to a source you chose to add, and the app
  never slips in people you didn't approve. ([Sourced provenance](../../spec/PNA_Spec.md#ac-17))
- When contacts from several places are combined into one person, each detail
  still remembers which place it came from. ([Multi-source dedup contract](../../spec/PNA_Spec.md#ac-prm-b))

---

## 3. Nothing leaves without you

> **Nothing about the people in your life ever leaves your device unless you
> decide to send it, understand what you're risking, and see exactly what's going
> out — first.**

- Your private notes are sealed shut by default and held to a higher standard
  than the ordinary contact facts (this is the same separation that keeps your
  data yours in the first place). ([Sovereign, sealed private layer](../../spec/PNA_Spec.md#ac-1))
- No server ever stores, keeps, or quietly backs up your private notes. ([No SaaS surface](../../spec/PNA_Spec.md#ac-2))
- The app is walled off from other web pages and programs, so they can't peek at
  what's inside. ([COOP/COEP required](../../spec/axes.md#rz-3))
- The app keeps its own behind-the-scenes signals to a bare minimum, so they
  can't be used to fish for who is or isn't in someone's circle. ([Anti-enumeration + abuse-bounded analytics](../../spec/PNA_Spec.md#ac-8))
- When you reach out to someone, *you* choose how the message travels, and secure
  options are offered — you're never forced onto a single channel. ([Communication-transport selection is user-driven](../../spec/PNA_Spec.md#ac-16))
- The app only offers ways of sending that can't read your message as it passes
  through. ([Transports cannot read message contents](../../spec/PNA_Spec.md#ac-18))
- Before anything goes out, you see the whole thing — who it's going to and
  everything attached — and you can change it or call it off, even when it's a
  message to a big group. ([User-visible payload before send](../../spec/PNA_Spec.md#ac-19))
- Handing your data to an AI counts as sending it out: a private AI that runs on
  your own device is the normal choice, an AI on the internet is used only if you
  approve it for that one request after seeing what it would get, and any outside
  AI must ask your permission each time before it can read your private notes. ([LLM calls over user data are transports](../../spec/PNA_Spec.md#ac-20), [Cloud AI clients require per-call consent for Private DB access via MCP](../../spec/PNA_Spec.md#ac-mcp-a))
- An AI helper can draft a message for you, but it can't actually send it —
  you're always the one who presses send. ([MCP Communications tools stage outreach; the workspace launches](../../spec/PNA_Spec.md#ac-mcp-b))

---

## 4. You won't lose it

> **Your private notes survive new phones, browser clean-ups, and app updates —
> and if something does go wrong, you can get your information back.**

- If the app updates but your saved information is from an older version, it won't
  get scrambled — the app holds off on changing anything until the two line up,
  while still letting you read what's there. ([Versioned cross-boundary handshake](../../spec/PNA_Spec.md#ac-4))
- The app quietly keeps a small, rolling set of recent backups of your private
  notes, so a recent copy is always there to restore. ([Auto-backup of private data on user-edit cadence](../../spec/PNA_Spec.md#ac-9))
- If two copies of the app try to use your information at the same time, it
  notices and tells you plainly instead of corrupting anything. ([Storage substrate detects concurrent access](../../spec/PNA_Spec.md#ac-11), [Single OPFS owner](../../spec/axes.md#rz-1), [Single-instance file-lock](../../spec/axes.md#rz-5))
- Refreshing your contacts never destroys the private notes you've built up, and
  you're shown in advance anything that would be left without a match. ([Re-imports of the Shared store are opt-in and non-destructive](../../spec/PNA_Spec.md#ac-10))

---

*These four are the plain-language version of the project's four formal goals,
and the bullets under each are its architectural promises restated without the
engineering vocabulary. The authoritative, technical version is the project
specification.*
