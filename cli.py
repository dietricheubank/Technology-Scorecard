"""Load fictional KPI metrics from JSON and produce a technology scorecard."""
import argparse
import json
from pathlib import Path
from app import Metric, render


def main():
    p = argparse.ArgumentParser(description="Generate a technology KPI scorecard")
    p.add_argument("input", help="Path to JSON metrics array")
    args = p.parse_args()
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("Input must be an array of metrics")
    metrics = [Metric(**item) for item in data]
    print(render(metrics))


if __name__ == "__main__":
    main()
