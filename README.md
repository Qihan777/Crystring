# ML_Crystring

Machine learning framework for crystal structure representation, property prediction, and generative modeling using Crystring, an invertible sequence-based representation of crystalline materials.

## Overview

ML_Crystring explores the application of machine learning techniques to crystalline materials using Crystring, a compact and invertible crystal structure representation that incorporates crystallographic symmetry information. By transforming crystal structures into sequence-based representations, the framework enables the use of modern machine learning models for materials property prediction, representation learning, and crystal generation.

The project integrates materials data from the Materials Project database and investigates how sequence-based representations can improve learning efficiency while preserving crystallographic information.

## Project Components

### CleanData

Data preprocessing and cleaning pipelines for Materials Project datasets.

### ML_BandGap

Machine learning models for band gap prediction from Crystring representations.

### ML_Ehull

Property prediction models for energy above hull and thermodynamic stability assessment.

### ML_LatticeParas

Prediction of lattice parameters from crystal structure representations.

### ML_regenerate_crystring

Tools for reconstructing crystal structures from Crystring representations and validating invertibility.

### Test_crystring

Validation scripts and benchmark tests for Crystring generation and reconstruction.

### Test Crystring Package

Unit tests and package verification utilities.

### Wyckoff_Positions_data

Reference data for Wyckoff positions used during structure encoding and decoding.

### group-subgroup_relationships

Crystallographic group-subgroup relationship datasets.

### group_subgroup_data

Supporting symmetry datasets for crystallographic operations.

### spglib_wyckoff

Utilities and datasets derived from spglib for symmetry analysis and Wyckoff position handling.

## Features

* Invertible crystal structure representation (Crystring)
* Crystal property prediction using machine learning
* Band gap prediction
* Energy-above-hull prediction
* Lattice parameter prediction
* Crystal structure reconstruction and validation
* Integration with Materials Project datasets
* Symmetry-aware encoding and decoding
* Support for generative modeling and representation learning

## Technologies

* Python
* PyTorch
* NumPy
* Pandas
* Pymatgen
* Spglib
* Materials Project API

## Research Motivation

Traditional crystal representations often struggle to balance structural fidelity, compactness, and compatibility with modern machine learning architectures. Crystring addresses these challenges by encoding crystallographic symmetry and atomic information into a sequence-based representation that is both machine-learning-friendly and invertible.

This framework investigates the use of Crystring for property prediction, crystal generation, and future large-scale pretraining of sequence models for materials discovery.

## Future Directions

* Transformer-based crystal language models
* Large-scale representation learning
* Generative crystal design
* Foundation models for materials science
* Integration with graph neural networks and multimodal materials AI systems
