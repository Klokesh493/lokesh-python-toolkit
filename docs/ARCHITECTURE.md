# Lokesh Python Toolkit architecture

Collect small repeatable checks for Markdown, task lists, schema drift, environment contracts, and JSONL.

```mermaid
flowchart LR
    A["Choose a utility from README"]
    B["Provide tool-specific fixture"]
    C["Execute the utility CLI"]
    D["Inspect findings and run isolated tests"]
    A --> B --> C --> D
```

## Operational boundaries

The tools run as independent utilities. Each folder defines its own input contract and exit behavior.
