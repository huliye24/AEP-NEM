# Versioning

## Protocol versioning

The AEP-NEM Protocol itself follows **Semantic Versioning (SemVer)**:

```
MAJOR.MINOR.PATCH
```

| Bump | Trigger |
|---|---|
| **MAJOR** | Breaking change to the protocol format. Old AEPs/NEMs may not validate against new schemas. |
| **MINOR** | New optional fields, new spec sections, new template types. Backward compatible. |
| **PATCH** | Clarifications, typo fixes, non-semantic corrections. |

**Current version:** `0.1.0` (Draft)

While in `0.x`, the protocol is considered unstable. Breaking changes may occur without a MAJOR bump. Once `1.0.0` is reached, SemVer is strictly enforced.

---

## AEP versioning

Each AEP is independently versioned:

```
MAJOR.MINOR.PATCH
```

- **MAJOR**: Scope change, structural rework, output format change
- **MINOR**: New tasks added, acceptance criteria expanded
- **PATCH**: Clarifications, bug fixes in task definitions

---

## NEM versioning

NEM versions are coupled to maturity levels:

| Maturity | Version Range | Gate Required |
|---|---|---|
| BASIC | v0.1.x | GATE-BASIC |
| STABLE | v0.3.x+ | GATE-STABLE |
| ADOPTED | v1.0.x+ | GATE-ADOPTED |
| REFACTORED | v2.0.x+ | GATE-REFACTOR |

NEM version bumps are triggered by absorbing new AEPs or passing maturity gates.

---

## Schema versioning

JSON schemas are versioned independently from the protocol:

- Schema versions track the format, not the protocol
- A schema `v0.1` can validate protocol `v0.1.x` AEPs
- Schema compatibility is tested through the validator test suite

---

## Release process

1. Proposals collected in GitHub Issues
2. Draft spec changes in a feature branch
3. Schema updated to match spec
4. Validator updated to match schema
5. Examples updated to demonstrate new format
6. PR merged → new protocol version tagged
7. Release notes published
