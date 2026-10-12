# QFF 2026 — Biomedical Quantum Classifier

## Problem Statement
**PS-Q1: Biomedical Signal Classifier**

## Objective
Build a hybrid quantum-classical Variational Quantum Classifier (VQC) to classify ECG heartbeat segments as normal or abnormal.

## Dataset
MIT-BIH Arrhythmia Database, Record 100.

## Methodology
1. Load and preprocess ECG signals.
2. Segment individual heartbeats.
3. Extract four numeric features.
4. Scale the features for quantum angle encoding.
5. Train a Variational Quantum Classifier.
6. Compare against Logistic Regression.
7. Benchmark circuit resources on Processor A and Processor B.
8. Evaluate noisy simulation results.

## Results
The CSV files in `results/tables/` and plots in `results/figures/` are
pre-existing artifacts. They have not yet been independently reproduced by
the current `src/` modules.

Insert the actual measured accuracy, precision, recall, F1 score, circuit depth, and CX counts after verifying the exported results.

## Limitations
The current experiment uses a beat-level split from a single ECG record. It does not establish generalization to unseen patients. Noisy simulator results are not real quantum hardware measurements.

## Reproducibility
The existing experiment notebook is
`notebooks/Biomedical_Quantum_Classifier.ipynb`. Dependencies are listed in
`requirements.txt`. Before rerunning the benchmark, verify the official
challenge configuration for both processor topologies and the dataset split.
