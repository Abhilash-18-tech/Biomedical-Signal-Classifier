"""Metric calculation helpers for classification predictions."""

from collections.abc import Sequence

from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score


def classification_metrics(
    y_true: Sequence[int], y_pred: Sequence[int]
) -> dict[str, float]:
    """Calculate standard binary metrics without applying result defaults."""
    if len(y_true) != len(y_pred):
        raise ValueError("y_true and y_pred must have equal lengths.")
    return {
        "accuracy": float(accuracy_score(y_true, y_pred)),
        "precision": float(precision_score(y_true, y_pred, zero_division=0)),
        "recall": float(recall_score(y_true, y_pred, zero_division=0)),
        "f1_score": float(f1_score(y_true, y_pred, zero_division=0)),
    }
