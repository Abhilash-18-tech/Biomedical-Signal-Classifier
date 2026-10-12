"""Plotting helpers for already-computed classification results."""

from collections.abc import Mapping
from pathlib import Path


def plot_metric_bars(
    metrics: Mapping[str, float],
    output_path: str | Path,
    *,
    title: str = "Classification metrics",
) -> Path:
    """Save a bar chart for supplied metrics; does not compute new results."""
    if not metrics:
        raise ValueError("At least one metric is required.")
    import matplotlib.pyplot as plt

    destination = Path(output_path)
    destination.parent.mkdir(parents=True, exist_ok=True)
    figure, axis = plt.subplots()
    axis.bar(list(metrics), list(metrics.values()))
    axis.set_title(title)
    axis.set_ylim(0, 1)
    axis.set_ylabel("Score")
    figure.tight_layout()
    figure.savefig(destination)
    plt.close(figure)
    return destination
