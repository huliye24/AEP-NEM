# Protocol Overview

## The six-layer architecture

AEP-NEM Protocol defines six interlocking layers, with PoEW, Gate, and Seal acting as the evidence and closure system inside the execution path:

```
┌─────────────────────────────────────────┐
│            E-ORGANISM                    │
│    Engineering Organism (the project)    │
│  ┌───────────────────────────────────┐  │
│  │         E-CHAINS                   │  │
│  │  Engineering Chains (main/branch)  │  │
│  │  ┌─────────────────────────────┐  │  │
│  │  │        NEMs                   │  │  │
│  │  │  Node Evolution Molecules    │  │  │
│  │  │  ┌───────────────────────┐  │  │  │
│  │  │  │       AEPs             │  │  │  │
│  │  │  │  Atomic Engineering    │  │  │  │
│  │  │  │  Packages              │  │  │  │
│  │  │  └───────────────────────┘  │  │  │
│  │  │  ┌───────────────────────┐  │  │  │
│  │  │  │  PoEW + GATE + SEAL    │  │  │  │
│  │  │  │ Proof, Gate, Closure   │  │  │  │
│  │  │  └───────────────────────┘  │  │  │
│  │  └─────────────────────────────┘  │  │
│  └───────────────────────────────────┘  │
└─────────────────────────────────────────┘
```

### Layer 1: AEP — Atomic Engineering Package

The smallest standard unit of engineering work. An AEP is a self-contained package containing:

- Task specification (`agent_spec.md`)
- Human-readable brief (`human_brief.md`)
- Task map with dependencies (`task_map.yaml`)
- Execution rules (`rules.md`)
- Validation criteria (`validation/`)
- Output directory (`outputs/`)
- Final report template (`reports/`)
- Manifest (`manifest.json`)

**Full spec:** [`specs/AEP_SPEC.md`](../specs/AEP_SPEC.md)

### Layer 2: NEM — Node Evolution Molecule

An evolvable engineering module composed of multiple AEPs. A NEM represents a node-level capability with:

- Versioned maturity levels (BASIC → STABLE → ADOPTED → REFACTORED)
- Internal AEP composition
- Interface contracts for external dependencies
- Evolution history

**Full spec:** [`specs/NEM_SPEC.md`](../specs/NEM_SPEC.md)

**NEM-18 profile:** [`specs/NEM_18_SPEC.md`](../specs/NEM_18_SPEC.md)

### Layer 3: E-Chain — Engineering Chain

A connected sequence of NEMs forming a main track or branch track. E-Chains define:

- Track type (main, feature, experiment, fix)
- NEM ordering and dependencies
- Branch/merge semantics
- Cross-track dependency resolution

**Full spec:** [`specs/E_CHAIN_SPEC.md`](../specs/E_CHAIN_SPEC.md)

**E-Chain 54 profile:** [`specs/E_CHAIN_54_SPEC.md`](../specs/E_CHAIN_54_SPEC.md)

### Layer 4: E-Organism — Engineering Organism

The living project as a whole — composed of multiple E-Chains, continuously growing and evolving. An E-Organism:

- Contains all E-Chains (main + branches)
- Tracks overall project health
- Defines cross-chain governance

### Layer 5: PoEW — Proof of Engineering Work

Verifiable evidence that engineering work was performed. Every AEP execution produces a PoEW record containing:

- Execution log
- Output artifacts
- Gate results
- Agent attribution
- Timestamp and duration
- Reproducibility hash

**Full spec:** [`specs/POEW_SPEC.md`](../specs/POEW_SPEC.md)

### Layer 6: Gate — Evolution Gate

A quality checkpoint that determines whether work passes to the next phase. Gates evaluate:

- Acceptance criteria (must-pass)
- Quality thresholds (should-pass)
- Stop conditions (must-stop)
- Evidence requirements

**Full spec:** [`specs/GATE_SPEC.md`](../specs/GATE_SPEC.md)

### Closure: Seal — Industrial completion

Seal is the closure layer that distinguishes a function that merely exists from work that is safe for downstream dependency.

```text
Function Complete -> PoEW -> Gate -> Seal Review -> Industrial Done
```

**Full spec:** [`specs/SEAL_PROTOCOL.md`](../specs/SEAL_PROTOCOL.md)  
**Industrial done spec:** [`specs/INDUSTRIAL_DONE_SPEC.md`](../specs/INDUSTRIAL_DONE_SPEC.md)

---

## The execution flow

```
1. Human defines strategic intent
2. AEP is generated as a self-contained package
3. AEP is dispatched to an executor (AI / human / cloud)
4. Executor produces PoEW (Proof of Engineering Work)
5. Gate evaluates the PoEW against acceptance criteria
6. Seal review checks evidence completeness and downstream safety
7. If passed: NEM absorbs the AEP and evolves
8. If failed: AEP is retried, refactored, reopened, or redefined
9. NEM connects into its E-Chain
10. E-Chain contributes to E-Organism growth
```

---

## Protocol vs. Implementation

AEP-NEM is a **protocol**, not a specific piece of software.

| What the protocol defines | What implementations do |
|---|---|
| Directory structure | Create and validate directories |
| File formats (manifest.json, task_map.yaml) | Parse, validate, execute |
| Gate rules | Evaluate, enforce, record |
| PoEW format | Generate, verify, accumulate |
| NEM versioning semantics | Tooling for version bumps and changelogs |

The minimum viable implementation is: a ZIP file with a standard directory structure. The first reference implementation is a Python CLI validator.

---

## Status

This protocol is **v0.1 Draft**. All specifications are open for discussion, contribution, and real-world testing. See [`governance/contribution.md`](../governance/contribution.md) for how to participate.
