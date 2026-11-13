"""Trend analysis of fictional KPI snapshots with direction-aware thresholds."""
from dataclasses import dataclass
from math import isfinite

@dataclass(frozen=True)
class Snapshot:
    period: str
    value: float

def analyze_trend(snapshots: list[Snapshot], target: float, direction: str) -> dict:
    if direction not in ("up","down"):
        raise ValueError("direction must be up or down")
    if not snapshots or any(not s.period or not isfinite(s.value) for s in snapshots):
        raise ValueError("nonempty finite snapshots required")
    if len({s.period for s in snapshots})!=len(snapshots):
        raise ValueError("periods must be unique")
    first,last=snapshots[0].value,snapshots[-1].value
    delta=round(last-first,4)
    meets=last>=target if direction=="up" else last<=target
    improving=delta>0 if direction=="up" else delta<0
    return {"periods":len(snapshots),"first":first,"latest":last,
            "change":delta,"direction":direction,"on_target":meets,
            "trend":"improving" if improving else "declining" if delta!=0 else "flat"}
