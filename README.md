# Torch Starter

## Overview

Torch Starter is a PyTorch project template based on Clean Architecture principles.
It is designed to provide researchers and developers a robust starting
point for PyTorch-based projects, ensuring a well-organized and scalable structure.

## Key Features

- **Hydra Configuration**: Efficient handling of complex configurations.
- **Organized Directory Structure**: Aligns with Clean Architecture for clarity and scalability.
- **Setup.py for Easy Installation**: Simplifies the installation process.
- **Continuous Deployment Pipeline**: Incorporates a basic CD pipeline using GitHub Actions (currently under development).

## Installation Guide

### Initial Setup

1. Use the template button and modify it according to your project requirements.
2. Update `setup.py` with your project information.

### Pre-commit Installation

Install pre-commit for local pipeline testing:

```bash
pip install pre-commit
pre-commit run --all-files
```

### Project Installation

Install your project in an editable mode:

```bash
pip install -e .
```

## Additional Resources

For an in-depth understanding of the Clean Architecture principles implemented
in this template, please refer to
[Bob Martin's original post](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html).

---

Torch Starter is committed to providing a solid foundation for PyTorch projects,
ensuring adherence to proven architectural practices.
