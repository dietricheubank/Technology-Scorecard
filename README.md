# Technology Scorecard

Data-backed executive IT scorecards with thresholds, trend direction and text reports.

## Run

Requires Python 3.11+ and no third-party dependencies.

```bash
cd Technology-Scorecard
python app.py
python -m unittest discover -s tests -v
```

## Design / scope

This standalone public project includes a Python implementation, a JSON command-line runner, synthetic examples, and automated checks in GitHub Actions.

The KPI definitions and thresholds are synthetic. A real scorecard needs documented data lineage, trend baselines, and governance for metric ownership.

## License

[MIT](LICENSE).

## Run from sample JSON

```bash
python cli.py examples/fictional-metrics.json
python -m unittest discover -s tests -v
```

Results are derived from the input dataset, with direction-aware thresholds (higher is better for availability; lower is better for restoration time). The metrics are **fictional** and do not represent any employer's service performance. GitHub Actions runs tests on pushes and pull requests.

## Historical KPI trend analysis

The [history module](history.py) compares successive KPI snapshots, calculates change, and evaluates improving or declining trends according to whether higher or lower values are better. [Trend tests](tests/test_history.py) cover both directions and invalid duplicate periods.

The current browser demo is still a single-period view; trend analysis is available in Python and is not yet integrated into the browser UI.
