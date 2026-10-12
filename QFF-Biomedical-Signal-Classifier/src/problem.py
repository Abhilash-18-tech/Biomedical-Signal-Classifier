"""Problem-level data structures for biomedical signal classification."""

from dataclasses import dataclass
from typing import Any, Mapping


@dataclass(frozen=True)
class SignalClassificationProblem:
    """Describe a classification problem without loading or fabricating data."""

    name: str
    signal_source: str
    class_labels: tuple[str, ...]
    feature_count: int
    metadata: Mapping[str, Any] | None = None

    def validate(self) -> None:
        """Raise ``ValueError`` when the problem definition is inconsistent."""
        if not self.name.strip():
            raise ValueError("Problem name must not be empty.")
        if not self.signal_source.strip():
            raise ValueError("Signal source must not be empty.")
        if len(self.class_labels) < 2:
            raise ValueError("At least two class labels are required.")
        if self.feature_count < 1:
            raise ValueError("feature_count must be positive.")
