# NEM Template

Copy this structure and rename `{NEM_ID}` to your NEM identifier.

## Directory structure

```
{NEM_ID}/
├── nem_manifest.yaml
├── nem_spec.md
├── interface.yaml
├── evolution_log.md
├── aeps/
│   └── README.md
├── gates/
│   └── gate_log.yaml
├── poew/
│   └── poew_log.yaml
└── dependencies/
    └── deps.yaml
```

---

## nem_manifest.yaml

```yaml
nem_id: "{NEM_ID}"
version: "0.1.0"
maturity: BASIC
title: "{TITLE}"
domain: "{DOMAIN}"
created: "{ISO_TIMESTAMP}"

maturity_history:
  - level: BASIC
    version: "0.1.0"
    achieved: "{ISO_TIMESTAMP}"
    gate: "GATE-BASIC-001"

constituent_aeps: []

interface:
  provides: []
  requires: []
```

---

## nem_spec.md

```markdown
# NEM Specification: {TITLE}

## Purpose
[What capability does this NEM provide?]

## Scope
[What is in scope? What is out of scope?]

## Maturity Roadmap
- [ ] BASIC (v0.1): [Core capability]
- [ ] STABLE (v0.3): [Production readiness]
- [ ] ADOPTED (v1.0): [Interface stability]

## Constituent AEPs
| AEP ID | Role | Status |
|---|---|---|
| | | |

## Dependencies
| NEM ID | Capability Required | Version |
|---|---|---|
| | | |
```

---

## interface.yaml

```yaml
provides:
  - capability: "{CAPABILITY_NAME}"
    version: "0.1.0"
    description: "{DESCRIPTION}"

requires:
  - capability: "{DEPENDENCY_NAME}"
    version: ">=0.1.0"
    description: "{DESCRIPTION}"
```

---

## evolution_log.md

```markdown
# Evolution Log: {NEM_ID}

## v0.1.0 — BASIC (2026-06-02)
- Initial creation
- Gate: GATE-BASIC-001 → PASS
- AEPs absorbed: none yet
```

---

## gates/gate_log.yaml

```yaml
gates:
  - gate_id: "GATE-BASIC-001"
    timestamp: "{ISO_TIMESTAMP}"
    result: PENDING
    target_maturity: BASIC
    evidence: []
```

---

## poew/poew_log.yaml

```yaml
poew_records: []
```

---

## dependencies/deps.yaml

```yaml
dependencies: []
```
