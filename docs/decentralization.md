# Decentralization

## The problem

Most engineering management systems assume a central authority: one tool, one server, one source of truth. This works for single organizations but breaks when:

- Multiple teams use different stacks
- Work is outsourced across organizational boundaries
- AI agents from different providers participate
- Engineering work spans public and private repositories
- Different centers want to publish, validate, and evolve tasks independently

## The AEP-NEM answer: multi-center publishing

AEP-NEM is designed for decentralization from the protocol level up.

### No central registry required

The protocol itself does not mandate a central registry. Anyone can:

1. **Publish** AEPs and NEMs from their own repository
2. **Validate** using the standard schemas (locally or via any validator)
3. **Reference** AEPs and NEMs across repositories using URIs
4. **Fork and evolve** independently while maintaining traceability

### How it works

```
Center A                   Center B                   Center C
(publishes NEMs)          (publishes NEMs)           (publishes NEMs)
     │                         │                          │
     └─────────────────────────┼──────────────────────────┘
                               │
                    AEP-NEM Protocol
                    (common language)
```

Each center:
- Maintains its own publishing authority
- Follows the same protocol format
- Signs its own PoEW records
- Can reference NEMs from other centers

### Cross-center references

A NEM from Center A can depend on a NEM from Center B:

```yaml
# In a NEM manifest
dependencies:
  - nem: "auth-service"
    version: ">=1.0.0"
    source: "github.com/center-b/auth-nems"
    nem_id: "NEM-AUTH-v1.0.0"
```

The protocol defines the reference format, not where the content lives.

### Trust model

Decentralization does not mean trust-free. It means:

1. **Verifiable**: Every PoEW can be independently verified
2. **Traceable**: Every AEP execution and Gate decision has a recorded trail
3. **Reproducible**: Anyone can re-execute an AEP and compare results
4. **Attributable**: Every contribution is signed and attributed

Trust is earned through accumulated verifiable proof, not through central authority.

---

## Multi-center publishing

See [`governance/multi-center-publishing.md`](../governance/multi-center-publishing.md) for the detailed publishing protocol.

---

## Future: decentralized network

Long-term, AEP-NEM envisions a decentralized engineering network where:

- AEPs are published, discovered, and executed across centers
- NEMs evolve through cross-center collaboration
- PoEW records form a verifiable global engineering graph
- Gates enforce quality without central gatekeepers
- Economic incentives align through PoEW-based reputation

This is aspirational. The current focus is on getting the protocol right.
