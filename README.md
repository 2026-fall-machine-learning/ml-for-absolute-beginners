# ML-for-Absolute-Beginners

Coding exercises from the book *Machine Learning for Beginners* by Oliver Theobald.

## UV environment setup (Python 3.12)

### 1. Install uv

```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### 2. Create and sync the project environment

From the repository root:

```powershell
uv sync --python 3.12
.\.venv\Scripts\Activate.ps1
```

This uses `pyproject.toml` to install all notebook dependencies into `.venv`.

### 3. Optional kernel registration

```powershell
python -m ipykernel install --user --name ml-absolute-beginners --display-name "Python (ml-absolute-beginners)"
```

## VS Code notebook workflow

1. Install the **Python** and **Jupyter** VS Code extensions.
2. Open this folder in VS Code.
3. Open any `.ipynb` notebook.
4. Click the kernel picker (top-right) and select:
   - `.venv\Scripts\python.exe`, or
   - **Python (ml-absolute-beginners)** if you registered the kernel.

## Daily use

```powershell
.\.venv\Scripts\Activate.ps1
```

If you add packages later:

```powershell
uv add <package-name>
uv sync
```

If VS Code shows **"Failed to start the Kernel"** with a `jedi` error, repair the kernel stack in the project venv:

```powershell
uv pip install --python .\.venv\Scripts\python.exe --upgrade ipykernel ipython jedi
```

If you see `ModuleNotFoundError: No module named 'scipy.sparse'`, reinstall the scientific stack in the same venv:

```powershell
uv pip install --python .\.venv\Scripts\python.exe --reinstall numpy scipy scikit-learn
```
