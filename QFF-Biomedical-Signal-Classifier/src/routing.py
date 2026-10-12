"""Routing helpers with explicit guards for unverified processor topology."""

from collections.abc import Iterable

from .processors import ProcessorTopology


def validate_logical_qubits(
    topology: ProcessorTopology, logical_qubits: Iterable[int]
) -> tuple[int, ...]:
    """Validate logical-qubit indices against a benchmark resource summary."""
    qubits = tuple(logical_qubits)
    if any(qubit < 0 or qubit >= topology.logical_qubits for qubit in qubits):
        raise ValueError(
            f"Logical qubits must be in range(0, {topology.logical_qubits})."
        )
    return qubits


def require_verified_connectivity(topology: ProcessorTopology) -> None:
    """Prevent routing against a processor until its official map is verified."""
    if not topology.configuration_verified:
        raise RuntimeError(
            f"Connectivity for {topology.name} is not verified against the "
            "official challenge settings."
        )
