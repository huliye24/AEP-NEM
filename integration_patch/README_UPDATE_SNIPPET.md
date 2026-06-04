# README Update Snippet

Add the following section to the main `README.md`.

---

## AEP Seal Protocol

AEP-NEM uses a formal Seal Protocol to distinguish ordinary functional completion from industrial-grade closure.

```text
Function Complete ≠ Seal Complete ≠ Industrial Done
```

- **Function Complete** means the task output exists.
- **PoEW** proves the work happened.
- **Gate** checks quality conditions.
- **Seal** verifies closure evidence.
- **Industrial Done** means the AEP can safely become a dependency for future NEM/E-Chain evolution.

Recommended status flow:

```text
DRAFT
→ IN_PROGRESS
→ FUNCTION_COMPLETE
→ EVIDENCE_PENDING
→ SEAL_REVIEW
→ SEAL_COMPLETE
→ INDUSTRIAL_DONE
```

See:

- `specs/SEAL_PROTOCOL.md`
- `specs/INDUSTRIAL_DONE_SPEC.md`
- `templates/SEAL_REPORT_TEMPLATE.md`
- `templates/SEAL_CHECKLIST_TEMPLATE.md`
- `schemas/seal_report.schema.json`
