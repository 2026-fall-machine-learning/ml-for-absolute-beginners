# Plan: uv-based Jupyter environment setup for notebook workflows

## Problem
This repository has multiple Jupyter notebooks but no reproducible Python environment definition yet (no `pyproject.toml`, `requirements*.txt`, `environment.yml`, or lockfile). We need a clean, repeatable setup using `uv` so notebooks run consistently.

## Current state (from repo scan)
- Notebooks are in the repository root (`*.ipynb`), with checkpoint copies in `.ipynb_checkpoints/`.
- Common imports across notebooks include: `pandas`, `scikit-learn`, `matplotlib`, and `seaborn`.
- `README.md` is minimal and does not document environment setup.
- Data files are present under `data/`.

## Chosen direction (confirmed)
- Deliverable scope: **docs-only** (no dependency manifest or lockfile changes in repo for now).
- Python target: **3.12**.
- Notebook frontend: **VS Code Jupyter extensions workflow**.
- Dependency strategy: **lighter/unlocked**.

## Proposed approach
Use `uv` as the package/environment manager and standardize on a project-local `.venv`. Document a clear VS Code-first workflow for creating/syncing the environment, installing baseline notebook packages, and selecting the correct interpreter/kernel in VS Code.

## Todos
1. **Define dependency baseline from notebooks**
   - Extract imports from notebook source cells (excluding checkpoint noise) and map to installable package names.
   - Build initial dependency set for runtime + notebook tooling (`ipykernel`, Jupyter frontend).

2. **Design uv + VS Code workflow for this repo**
   - Specify canonical commands for first-time setup and dependency sync with `uv`.
   - Include interpreter/kernel selection steps in VS Code (Python + Jupyter extensions).
   - Include optional `ipykernel` registration command for notebook kernel name consistency.

3. **Plan documentation updates**
   - Update `README.md` with a short "UV environment setup" section.
   - Add concise "Open in VS Code" and "Select interpreter/kernel" steps.
   - Include troubleshooting notes for common Windows + VS Code issues.

4. **Validation plan**
   - Verify documented `uv` commands create/use `.venv` with Python 3.12.
   - Verify VS Code can select the environment for notebooks.
   - Verify package list covers imports used in notebooks.

## Notes
- This plan intentionally avoids adding project manifests/lockfiles because scope is docs-only.
- If later you want reproducibility for collaborators, the next step would be moving to `pyproject.toml` + `uv.lock`.
