# fellows_local_db

**Maintainer:** Rich Bodo (https://github.com/richbodo/fellows_local_db)
**License:** see upstream repo
**First accepted:** PNA Spec v0.1, <YYYY-MM-DD pending>
**Status:** active (placeholder — Software Heritage SWHID and full attestation pending Phase 5 of the reorganization plan)

## Summary

`fellows_local_db` is the first PNA reference design — a Directory Archive PNA realizing the Knack-export → static-PWA + magic-link distribution flavor. It is the design from which most of the v0.1 spec was distilled. The canonical repo lives at https://github.com/richbodo/fellows_local_db; its Architecture document is at `docs/Architecture.md` upstream.

## Axis picks at first acceptance

`distribution:web-bundle-with-magic-link + storage:opfs-sqlite-wasm + ingestion:single-source-static-mirror + workspace-shell:vanilla-js-spa + comms:mailto-only + mcp-exposure:shared+private+comms`

## Contributions to the spec

The bulk of PNA Spec v0.1 — every universal AC except those flagged `[draft]`, every sub-contract under `WS-`, `ST-`, `SH-`, `PR-`, `DB-`, `IN-`, `CO-`, `DI-`, and the realized axis picks in `axes.md` — derives from learnings on this design. The detailed contribution list and the SWHID are backfilled in Phase 5 of `plans/reorganization-plan.md`.

## Architectural learnings

Pending Phase 5 backfill. The PWA-doesn't-work-for-most-PNAs insight from real user feedback is the canonical one — captured today in the universal architectural commitments via AC-3, AC-12, AC-13, and the `dist:pwa`-triggered AC-14.

## Reproducibility notes

See upstream repo's README for current build instructions. SWHID-archived snapshot will be added in Phase 5.

## Architecture document

Pending Phase 5: a copy of upstream `docs/Architecture.md` lands here as `Architecture.md`, with the AC attestation table backfilled (Realization, Verification, Status per applicable AC).
