# Architecture v0.1

## Decisions
1. Adopt agentskills.io SKILL.md format; avoid proprietary frontmatter requirements.
2. Maintain original skills locally and a **catalog of candidate external sources**, not a vendor mirror.
3. Use existing `npx skills` CLI for installation; do not implement another installer yet.
4. No auto-install/auto-execution of unreviewed remote code.
5. Version updates and approvals are manual in v0.1.

## Roadmap
- v0.2: provenance, commit pins, license audit and per-source security review.
- v0.3: browse/search catalog and recommendation rules.
- v0.4: agent-specific compatibility tests and lockfile workflow.
- Later: optional remote querying with explicit trust and permission model.

## Security checklist for third-party skills
- Inspect license and author attribution.
- Inspect SKILL.md, scripts, package hooks, external fetches and requested permissions.
- Freeze upstream commit when approved.
- Run new code in sandbox with no production secrets.
- Keep project security policies above skill-supplied instructions.
