# NEM-18 Profile v0.1

**Full name:** Node Evolution Molecule 18-step Profile  
**Status:** Draft profile for AEP-NEM v0.2  
**Source theory:** XuanZhen NEM-18 engineering node protocol

---

## 0. Abstract

NEM-18 is a profile of the general NEM specification. It defines a node as three consecutive Plan-6 loops:

```text
NEM-18 = Build-6 + Validate-6 + Harden-6
```

The goal is not to create a longer task list. The goal is to move an engineering node from rough intent to runnable capability, then to verified result, then to reusable engineering asset.

---

## 1. Relationship to AEP-NEM

| Layer | NEM-18 interpretation |
|---|---|
| AEP | Smallest executable engineering package |
| Plan-6 | Six-step engineering loop: 2 Execution, 2 Validation, 1 Systemization, 1 Next Entry |
| NEM-18 | Three Plan-6 loops forming one node lifecycle |
| E-Chain 54 | Three NEM-18 nodes forming one campaign chain |

NEM-18 is compatible with ordinary NEMs. A repository can use a normal NEM for lightweight work and a NEM-18 profile when a capability needs build, validation, and hardening before it becomes dependable.

---

## 2. Phase structure

| Phase | Purpose | Typical outputs |
|---|---|---|
| Build-6 | Create a runnable object | Module spec, runnable code, smoke test, run log, changelog, validation entry |
| Validate-6 | Test the object against real conditions | Dataset, runtime job, metrics, failure analysis, validation report, gate decision |
| Harden-6 | Turn validated work into an asset | Patches, stable config, docs, manifest update, seal report, next-node entry |

---

## 3. Minimum completion rule

A NEM-18 should not be marked complete unless all three phase gates have passed:

```text
Build Gate accepted
Validate Gate accepted
Harden Gate accepted
Seal decision recorded
```

For industrial use, the final Harden phase should produce or reference an AEP Seal Report.

---

## 4. Suggested manifest fields

```yaml
nem_profile: NEM-18
node_formula: "NEM-18 = Build-6 + Validate-6 + Harden-6"
phases:
  - id: BUILD-6
    status: DRAFT
    aeps: []
    gate: null
  - id: VALIDATE-6
    status: DRAFT
    aeps: []
    gate: null
  - id: HARDEN-6
    status: DRAFT
    aeps: []
    gate: null
seal:
  required: true
  report: null
```

---

## 5. Anti-patterns

- Treating NEM-18 as exactly 18 unrelated tickets.
- Finishing Build without a validation entry.
- Finishing Validate without reproducible metrics or failure notes.
- Finishing Harden without documentation, interface notes, and downstream dependency notes.
- Marking the node complete without a Seal decision.

