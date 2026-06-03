# E-Chain Specification v0.1

**Full name:** Engineering Chain Specification
**Version:** v0.1 Draft
**Status:** Draft — open for feedback

---

## 0. Abstract

E-Chain (Engineering Chain) defines how NEMs are connected into linear sequences forming main tracks and branch tracks. E-Chains provide the topology for engineering work: ordering, branching, merging, and cross-track dependency resolution.

---

## 1. Definition

> **E-Chain is a connected sequence of NEMs forming a main track or branch track.**

If AEPs are atoms and NEMs are molecules, E-Chains are the chains that connect molecules into structured pathways.

---

## 2. Track Types

| Type | Purpose | Behavior |
|---|---|---|
| **main** | Primary project progression | Linear, ordered, always forward |
| **feature** | New capability development | Branches from main, merges back |
| **experiment** | Exploration and prototyping | May or may not merge |
| **fix** | Bug fix or patch | Branches from a specific NEM version, merges back |

---

## 3. E-Chain Structure

```yaml
# echain.yaml
chain_id: "MAIN-MOODIFY"
chain_type: main
project: "Moodify"

nems:
  - nem_id: "NEM-MRS"
    version: "0.1.0"
    order: 1
    gates_passed: ["GATE-BASIC"]

  - nem_id: "NEM-TIDECYCLE"
    version: "0.1.0"
    order: 2
    gates_passed: ["GATE-BASIC"]

  - nem_id: "NEM-WEATHER"
    version: "0.1.0"
    order: 3
    gates_passed: ["GATE-BASIC"]
```

---

## 4. Branching Model

```
main:    [NEM-1] → [NEM-2] → [NEM-3] → [NEM-4]
                          ↘         ↗
feature:                   [NEM-F1]
```

Branch rules:
- A branch track starts from a specific NEM version on its parent track
- A branch track may merge back into any downstream NEM on the parent
- Merge requires a Gate evaluation
- Conflicts between tracks are resolved at the NEM dependency level

---

## 5. Cross-Track Dependencies

A NEM on one track can depend on a NEM from another track:

```yaml
# In NEM-MRS nem_manifest.yaml
dependencies:
  - nem: "NEM-TIDECYCLE"
    track: "MAIN-MOODIFY"
    version: ">=0.3.0"
```

Cross-track dependencies create a DAG (directed acyclic graph) across the entire E-Organism.

---

## 6. E-Chain Operations

| Operation | Description |
|---|---|
| **append** | Add a NEM to the end of a chain |
| **insert** | Insert a NEM between existing NEMs (destabilizes downstream) |
| **branch** | Create a new track from a NEM |
| **merge** | Merge a branch track back into its parent |
| **reorder** | Change NEM ordering (requires re-validation) |
| **archive** | Mark a track as read-only |

---

## 7. Chain Validation

Before an E-Chain is considered valid:

1. All constituent NEMs must have passed their own Gates
2. NEM ordering must respect dependency constraints
3. Cross-track references must be resolvable
4. No circular dependencies
5. Merge points must have merge Gate results

---

## 8. E-Chain vs. Git Branch

E-Chains are NOT Git branches, though they can map to them:

| Concept | E-Chain | Git Branch |
|---|---|---|
| Unit | NEM (molecule of AEPs) | Commit (diff) |
| Branching | Semantic (capability branching) | Code-level |
| Merge | Gate-evaluated capability merge | Code merge |
| History | Evolution log + PoEW | Commit history |

A project may choose to map E-Chains to Git branches, but the protocol does not require it.
