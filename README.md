# AEP-NEM Protocol

**AEP-NEM Engineering Protocol — an open protocol for AI-native engineering tasks, node evolution, gates, and proof of engineering work.**

---

## What is AEP-NEM?

AEP-NEM is a complete AI-native engineering collaboration protocol. It redefines how engineering work is structured, executed, verified, and evolved when AI agents, humans, and automated systems collaborate on complex projects.

### Core concepts

| Layer | Abbrev | Name | Role |
|---|---|---|---|
| Task package protocol | **AEP** | Atomic Engineering Package | Distributable minimal engineering task package protocol |
| Project node protocol | **NEM** | Node Evolution Molecule | Evolvable project node protocol composed of multiple AEPs |
| Main/branch chain | **E-Chain** | Engineering Chain | Connected sequence of NEMs forming a track |
| Project whole | **E-Organism** | Engineering Organism | The living project composed of E-Chains |
| Proof of work | **PoEW** | Proof of Engineering Work | Verifiable evidence that work was done |
| Quality gate | **Gate** | Evolution Gate | Acceptance checkpoint before next phase |
| Closure layer | **Seal** | AEP Seal Protocol | Evidence review that moves work from function-complete to industrial-done |

### One-sentence definition

> AEP is the distributable minimal engineering task package protocol; NEM is the evolvable project node protocol composed of multiple AEPs. PoEW proves the work, Gate decides evolution, and Seal closes the work for downstream dependency.

---

## Repository structure

```
aep-nem-protocol/
├── README.md
├── LICENSE
├── docs/              # Philosophy, overview, decentralization, glossary
├── specs/             # Formal specifications for each protocol layer
├── templates/         # Reusable templates for AEP, NEM, E-Chain, PoEW
├── schemas/           # JSON schemas for validation
├── examples/          # Real-world examples (moodify/, generic/)
├── governance/        # Contribution, versioning, multi-center publishing
├── tools/             # Reference validation tools
└── integration_patch/ # Upstream merge snippets and patch notes
```

---

## Quick start

0. **中文协议入口**: [`docs/aep-nem/README.md`](docs/aep-nem/README.md)
1. **Read the overview**: [`docs/protocol-overview.md`](docs/protocol-overview.md)
2. **Understand the philosophy**: [`docs/philosophy.md`](docs/philosophy.md)
3. **Check the glossary**: [`docs/glossary.md`](docs/glossary.md)
4. **Read the specs**: Start with [`specs/AEP_SPEC.md`](specs/AEP_SPEC.md)
5. **Use a template**: [`templates/AEP_TEMPLATE.md`](templates/AEP_TEMPLATE.md)
6. **See an example**: [`examples/generic/AEP-EXAMPLE-001.md`](examples/generic/AEP-EXAMPLE-001.md)

---

## Industrial closure

AEP-NEM uses a formal Seal Protocol to distinguish ordinary functional completion from industrial-grade closure.

```text
Function Complete != Seal Complete != Industrial Done
```

- **Function Complete** means the task output exists.
- **PoEW** proves the work happened.
- **Gate** checks quality conditions.
- **Seal** verifies closure evidence.
- **Industrial Done** means the AEP can safely become a dependency for future NEM/E-Chain evolution.

Recommended status flow:

```text
DRAFT
-> IN_PROGRESS
-> FUNCTION_COMPLETE
-> EVIDENCE_PENDING
-> SEAL_REVIEW
-> SEAL_COMPLETE
-> INDUSTRIAL_DONE
```

See [`specs/SEAL_PROTOCOL.md`](specs/SEAL_PROTOCOL.md), [`specs/INDUSTRIAL_DONE_SPEC.md`](specs/INDUSTRIAL_DONE_SPEC.md), and [`templates/SEAL_REPORT_TEMPLATE.md`](templates/SEAL_REPORT_TEMPLATE.md).

---

## Protocol profiles

- **NEM-18**: a node-level profile that organizes one NEM as three Plan-6 loops: Build, Validate, and Harden. See [`specs/NEM_18_SPEC.md`](specs/NEM_18_SPEC.md).
- **E-Chain 54**: a campaign-level chain profile composed of Probe NEM-18, Build NEM-18, and System NEM-18. See [`specs/E_CHAIN_54_SPEC.md`](specs/E_CHAIN_54_SPEC.md).

---

## Status

**Version:** v0.2 Draft  
**Created:** 2026-06-02  
**Updated:** 2026-06-04

This protocol is in early draft stage. v0.2 adds industrial closure through Seal, plus NEM-18 and E-Chain 54 profiles for larger AI-native engineering cycles. All specs, templates, and schemas are open for feedback, contribution, and real-world testing.

---

## License

Apache License 2.0 — see [LICENSE](LICENSE)
