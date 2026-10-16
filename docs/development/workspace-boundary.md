# Workspace boundary

Established by T0001 ([contract C-T0001-v1](../contracts/C-T0001-v1.md)). The repository owner approved it on 16 October 2026. The machine-readable inventory is [workspace-inventory.json](workspace-inventory.json).

## Two inventories

| Inventory | Where it lives | What it holds |
|---|---|---|
| **Private custody** | Only on the owner's computer, in the primary workspace `D:\Desktop\Opshub` | 70 protected originals: all 38 `source/` files, 15 verbatim text extracts of source documents, 4 rendered source-PDF pages and 13 captured Gentry production JS files. 3 compiled `.pyc` caches are excluded as generated. |
| **Trackable** | Git, every clone, GitHub | Everything else: the 225 other protected Phase 1–5 documents and evidence, Phase 6 planning, and future code, tests and contracts |

Private-custody files are never committed, pushed, copied into fixtures, pasted into prompts or attached to reviews. They are also absent from Git history: the owner had the history rewritten on 16 October 2026. Their paths and SHA-256 digests stay listed in the inventory, so their integrity can still be checked where they exist.

## What may be tracked

- **Root files:** `.gitattributes`, `.gitignore`, `AGENTS.md`, `CLAUDE.md`, `package.json`, `package-lock.json`.
- **Root directories:** `.github/`, `apps/`, `docs/`, `evidence/`, `ops/`, `packages/`, `scripts/`, `tests/`.

Adding any other root-level file or directory, or changing an ignore rule, needs a versioned amendment of C-T0001 under the `root-contracts` lock. This keeps files like `.npmrc` tokens or ad-hoc dumps out by default.

## Ignore rules

`.gitignore` excludes the private-custody paths, secrets and credentials (`.env*` except `.env.example`, `.npmrc`, keys and certificates, `secrets/`), dependencies and build/test output, and Python caches.

Fixtures follow one convention:
- Synthetic fixtures live under `tests/fixtures/` and are tracked.
- Anything real or private goes under `tests/fixtures/private/` or is named `*.private.*`; both are ignored.

## Line endings

`.gitattributes` stores ordinary text as LF everywhere, whatever a machine's `core.autocrlf` is. Protected Phase 1–5 documents and evidence, plus the Phase 6 baseline file, are byte-exact (`-text`). As a result, any checkout reproduces the SHA-256 digests in `evidence/implementation/phase6-input-baseline.json`.

## Node baseline

The repository targets **Node 24 LTS** (`"engines": {"node": ">=24 <25"}`). The local check ran on Node v24.16.0 and npm 11.13.0. That is an observation, not a pin: the exact patch and package versions are qualified and pinned by T0002. T0001 installs no packages and creates no lockfile.

## Checks

```bash
npm run test:t0001
```

On the owner's computer, the original-integrity check also runs with the custody root:

```bash
OPSHUB_CUSTODY_ROOT=D:/Desktop/Opshub npm run test:t0001
```

Without the custody files present, that check reports NOT_CHECKED (skipped), never PASS. The Phase 6 plan verifier (`python evidence/implementation/verify_plan.py`) works in any checkout. It reports private-custody files absent from a clone as `protected_in_private_custody_not_checked`.
