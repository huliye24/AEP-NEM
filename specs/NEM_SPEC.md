# NEM Specification v0.1

**Full name:** Node Evolution Molecule Specification
**Version:** v0.1 Draft
**Status:** Draft — open for feedback

---

## 0. Abstract

NEM (Node Evolution Molecule) is the standard format for an evolvable engineering module composed of multiple AEPs. A NEM represents a node-level capability unit that can be versioned, upgraded, validated, refactored, depended upon, and reused across AI-native engineering systems.

---

## 1. Definition

> **NEM is an evolvable engineering module composed of multiple AEP engineering atoms.**

A NEM is not a one-time task list. It is a molecular engineering capability unit that grows through absorbing AEPs and evolving through maturity levels.

---

## 2. Key Properties

| Property | Description |
|---|---|
| **Evolvable** | Absorbs new AEPs to gain capabilities |
| **Versioned** | Has a version number and maturity level |
| **Validatable** | Can be independently verified |
| **Refactorable** | Can be restructured while maintaining interface |
| **Dependable** | Can be depended on by other NEMs |
| **Reusable** | Can be used across different E-Chains and projects |

---

## 3. What NEM Is NOT

- Not a task list
- Not a one-time work order
- Not a single Markdown file
- Not a single AEP
- Not a Git branch (though it may correspond to one)
- Not a microservice (though it may map to one)
- Not a Jira epic (though it replaces the concept)

---

## 4. NEM Structure

```
{NEM_ID}/
├── nem_manifest.yaml          # NEM metadata and version
├── nem_spec.md                # NEM capability specification
├── interface.yaml             # Public interface contract
├── evolution_log.md           # Chronological evolution record
│
├── aeps/                      # Constituent AEPs
│   ├── {AEP_ID_1}/
│   ├── {AEP_ID_2}/
│   └── ...
│
├── gates/                     # Gate results for this NEM
│   └── gate_log.yaml
│
├── poew/                      # Aggregated proof of engineering work
│   └── poew_log.yaml
│
└── dependencies/              # External NEM dependencies
    └── deps.yaml
```

---

## 5. nem_manifest.yaml

```yaml
nem_id: "NEM-TIDECYCLE"
version: "0.1.0"
maturity: BASIC
title: "Tide Cycle Prediction Module"
domain: "environmental"
created: "2026-06-02T00:00:00Z"

maturity_history:
  - level: BASIC
    version: "0.1.0"
    achieved: "2026-06-02T00:00:00Z"
    gate: "GATE-BASIC-001"

constituent_aeps:
  - aep_id: "AEP-TIDE-DATA-001"
    role: "data_ingestion"
  - aep_id: "AEP-TIDE-MODEL-001"
    role: "core_algorithm"
  - aep_id: "AEP-TIDE-GATE-CALIBRATION-001"
    role: "quality_gate"

interface:
  provides:
    - "tide_prediction"
    - "tide_visualization"
  requires:
    - "weather_data"
    - "astronomical_data"
```

---

## 6. Maturity Levels

| Level | Version Range | Meaning |
|---|---|---|
| **BASIC** | v0.1.x | Core capability exists. Foundational AEPs complete. |
| **STABLE** | v0.3.x+ | Production-ready. All quality gates passed. |
| **ADOPTED** | v1.0.x+ | Depended on by other NEMs. Stable interface contract. |
| **REFACTORED** | v2.0.x+ | Redesigned based on accumulated learning. |

---

## 7. NEM Evolution

A NEM evolves by absorbing completed AEPs:

```
NEM v0.1.0 (BASIC)
    │
    ├── AEP-001: core capability
    ├── AEP-002: enhancement
    ├── GATE-STABLE: quality check
    │
    ▼
NEM v0.3.0 (STABLE)
    │
    ├── AEP-003: performance optimization
    ├── AEP-004: integration
    ├── GATE-ADOPTED: adoption check
    │
    ▼
NEM v1.0.0 (ADOPTED)
```

Each evolution step:
1. One or more AEPs are executed
2. PoEW is generated
3. Gate evaluates the work
4. NEM version and maturity are updated
5. Evolution log is appended

---

## 8. Interface Contract

Every NEM declares a public interface:

```yaml
# interface.yaml
provides:
  - capability: "tide_prediction"
    version: "1.0.0"
    endpoint: "predict(lat, lon, timestamp) -> TidePrediction"

requires:
  - nem: "NEM-WEATHER"
    capability: "weather_forecast"
    version: ">=0.3.0"
```

The interface contract is the stable boundary. Internal AEPs can be refactored, replaced, or reordered — as long as the interface is maintained.

---

## 9. Dependency Model

NEMs can depend on other NEMs. Dependencies are:

- **Version-pinned**: `">=0.3.0"`, `"^1.0.0"`
- **Capability-based**: "I need `weather_forecast`, not a specific NEM"
- **Cross-center**: Can reference NEMs from other publishing centers

---

## 10. Naming Convention

```
NEM-{DOMAIN}

Examples:
  NEM-TIDECYCLE       # Tide prediction module
  NEM-MRS             # Mood Recommendation System
  NEM-AUTH            # Authentication module
```
