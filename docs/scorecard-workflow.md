# Technology scorecard measurement workflow

```mermaid
flowchart TD
  A[Choose service outcomes] --> B[Define KPI and direction]
  B --> C[Document target]
  C --> D[Collect and validate measurements]
  D --> E[Evaluate higher-is-better or lower-is-better]
  E --> F[Generate scorecard]
  F --> G[Explain variances and uncertainty]
  G --> H[Assign corrective actions]
  H --> I[Review trends next period]
```

The implementation currently covers evaluation and text reporting; measurement ingestion, owner assignment, trends and action tracking are future enhancements. All included examples are fictional.

Run `python cli.py examples/fictional-metrics.json`.
