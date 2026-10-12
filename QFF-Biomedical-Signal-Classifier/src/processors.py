"""Processor configuration and resource summaries.

The benchmark resource summaries are historical observations. A processor
configuration is not considered runnable until its official topology is
provided and validated.
"""

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping


@dataclass(frozen=True)
class ProcessorTopology:
    """Resource summary; connectivity is intentionally not inferred."""

    name: str
    physical_qubits: int
    logical_qubits: int
    circuit_depth: int
    cx_count: int
    two_qubit_gate_count: int
    operation_counts: dict[str, int]
    configuration_verified: bool = False


def load_processor_config(path: str | Path) -> dict[str, Any]:
    """Load and validate a processor configuration without inventing values."""
    source = Path(path)
    if not source.exists():
        raise FileNotFoundError(f"Processor configuration not found: {source}")
    if source.stat().st_size == 0:
        raise ValueError(f"Processor configuration is empty: {source}")

    try:
        with source.open(encoding="utf-8") as handle:
            config = json.load(handle)
    except json.JSONDecodeError as error:
        raise ValueError(f"Invalid JSON in processor configuration: {source}") from error

    if not isinstance(config, dict):
        raise ValueError("Processor configuration must be a JSON object.")

    required_fields = {"name", "num_qubits", "coupling_map", "basis_gates"}
    missing_fields = sorted(required_fields.difference(config))
    if missing_fields:
        raise ValueError(
            "Processor configuration is missing required fields: "
            + ", ".join(missing_fields)
        )

    name = config["name"]
    num_qubits = config["num_qubits"]
    coupling_map = config["coupling_map"]
    basis_gates = config["basis_gates"]
    if not isinstance(name, str) or not name.strip():
        raise ValueError("Processor 'name' must be a non-empty string.")
    if not isinstance(num_qubits, int) or isinstance(num_qubits, bool) or num_qubits < 1:
        raise ValueError("Processor 'num_qubits' must be a positive integer.")
    if not isinstance(coupling_map, list):
        raise ValueError("Processor 'coupling_map' must be a list of edges.")
    if not isinstance(basis_gates, list) or not all(
        isinstance(gate, str) and gate for gate in basis_gates
    ):
        raise ValueError("Processor 'basis_gates' must be a list of gate names.")

    for edge in coupling_map:
        if (
            not isinstance(edge, list)
            or len(edge) != 2
            or any(
                not isinstance(qubit, int) or isinstance(qubit, bool)
                for qubit in edge
            )
            or any(qubit < 0 or qubit >= num_qubits for qubit in edge)
        ):
            raise ValueError(
                "Each coupling-map edge must contain two valid physical-qubit indices."
            )

    return config


def benchmark_topologies() -> dict[str, ProcessorTopology]:
    """Return the observed benchmark summaries for Processors A and B."""
    return {
        "Processor A": ProcessorTopology(
            name="Processor A",
            physical_qubits=5,
            logical_qubits=4,
            circuit_depth=57,
            cx_count=17,
            two_qubit_gate_count=17,
            operation_counts={"rz": 63, "sx": 34, "cx": 17},
        ),
        "Processor B": ProcessorTopology(
            name="Processor B",
            physical_qubits=9,
            logical_qubits=4,
            circuit_depth=25,
            cx_count=8,
            two_qubit_gate_count=8,
            operation_counts={"rz": 38, "sx": 22, "cx": 8},
        ),
    }
