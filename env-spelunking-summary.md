# Environment Spelunking Summary

Date: 2026-07-24
Project: ML-for-Absolute-Beginners

## What `uv pip list` shows

- `uv pip list` shows packages that are already installed in the environment `uv` selected.
- It does not show hypothetical packages that would be installed.
- In a project folder with `.venv`, `uv` often auto-detects and uses that environment even if the shell is not manually activated.

## Why packages still appear when `.venv` is "not active"

- Activation (`source .venv/bin/activate`) mainly changes shell `PATH` and prompt.
- `uv` can target the project environment directly without shell activation.
- So seeing `.venv` packages in `uv` commands is expected behavior.

## Deactivating environments

- Standard virtual environment deactivation command:

```sh
deactivate
```

- For Conda environments:

```sh
conda deactivate
```

## Where `deactivate` comes from

- `deactivate` is usually a shell function defined by the activation script.
- It is loaded when you run `source .venv/bin/activate`.
- It is not usually a standalone executable on `PATH`.

Useful checks:

```sh
type deactivate
whence -f deactivate   # zsh
echo "$VIRTUAL_ENV"
```

To inspect the defining script:

```sh
cat .venv/bin/activate
```

## Python version inventory snapshot (from `uv python list`)

- Installed and available locally:
- Homebrew CPython 3.14.6
- uv-managed CPython 3.14.3
- uv-managed CPython 3.12.13
- macOS system CPython 3.9.6
- Many other versions are listed as downloadable, not installed.

## Is this setup messy?

- Overall: reasonably clean for active Python work.
- Typical and healthy pattern: one Homebrew Python, some uv-managed versions, and system Python.
- Only "messy" if your goal is strict minimalism.

## 3.12 vs 3.14 decision for this ML project

- Choosing Python 3.12 was a good stability-first decision.
- For ML/data stacks, 3.11/3.12 often gives smoother compatibility than very new releases.
- 3.14 should be adopted when you specifically need it and your dependency stack is verified on it.

## What Python constraint in `pyproject.toml` means

- Python constraints control compatibility, not "always older dependency versions."
- Resolvers still try to pick the newest package versions that satisfy:
- your dependency constraints
- your Python version constraint
- the interpreter used for installation

Examples:

- `>=3.12` allows 3.12, 3.13, 3.14, etc.
- To stay strictly on 3.12, use `==3.12.*` or `>=3.12,<3.13`.

## Practical policy going forward

1. Keep this repo on Python 3.12 unless there is a clear feature need for 3.14.
2. Treat 3.14 migration as planned (test and dependency validation first).
3. Avoid using system Python for project package management.
