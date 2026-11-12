# Lokesh Python Toolkit architecture

Collect small repeatable checks for Markdown, task lists, schema drift, environment contracts, and JSONL.

```mermaid
flowchart LR
    N0["Utility-specific sample"]
    N1["Dedicated Python CLI"]
    N2["Findings and isolated unit tests"]
    N0 --> N1 --> N2
```

## Operational boundaries

The tools run as independent utilities. Each folder defines its own input contract and exit behavior.
