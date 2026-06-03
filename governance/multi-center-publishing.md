# Multi-Center Publishing

## Concept

AEP-NEM is designed for **multi-center publishing**: multiple independent authorities can publish, validate, and evolve AEPs and NEMs without a central registry.

Each center:
- Maintains its own namespace
- Follows the same protocol format
- Signs its own PoEW records
- Can reference NEMs from other centers

---

## Center Identity

A center is identified by a URI:

```
github.com/{org}/{repo}
gitlab.com/{org}/{repo}
center.example.org/{name}
```

Each center MUST declare its identity in a `.aep-nem/center.yaml` file:

```yaml
center_id: "github.com/team-moodify/moodify-o3is"
name: "Moodify Engineering Center"
contact: "engineering@moodify.example.org"
namespaces:
  - "moodify"
  - "tide"
```

---

## Publishing an AEP

To publish an AEP:

1. Package the AEP directory following the AEP spec
2. Place it in your center's repository under `aeps/{AEP_ID}/`
3. Ensure `manifest.json` validates against the AEP schema
4. Tag the commit with `aep/{AEP_ID}/v{version}`
5. (Optional) Register in a public AEP-NEM registry

## Publishing a NEM

To publish a NEM:

1. Assemble the NEM directory following the NEM spec
2. Ensure all constituent AEPs have passed their gates
3. Ensure `nem_manifest.yaml` validates against the NEM schema
4. Tag the commit with `nem/{NEM_ID}/v{version}`
5. (Optional) Register in a public AEP-NEM registry

---

## Cross-Center References

A NEM can reference AEPs or NEMs from another center:

```yaml
# In nem_manifest.yaml
constituent_aeps:
  - aep_id: "AEP-TIDE-DATA-001"
    role: "data_ingestion"
    source: "github.com/center-tide/tide-aeps"
    version: "0.1.0"
```

The reference format:
```
{center_uri} / aeps / {aep_id} @ {version}
{center_uri} / nems / {nem_id} @ {version}
```

---

## Trust Model

Multi-center publishing does not require trust between centers. It requires **verifiability**:

1. Any center can download and validate any AEP using the standard schema
2. Any center can re-execute any AEP and compare PoEW hashes
3. Any center can replay gate criteria against recorded outputs
4. Trust is earned through accumulated verifiable proof, not authority

---

## Discovery (Future)

v0.1 does not define a discovery mechanism. Future versions may include:

- A voluntary registry protocol
- A distributed discovery service
- Cross-center search and indexing

For now, discovery is out of band: centers link to each other, and references are resolved at read time.
