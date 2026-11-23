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

## Comparing k-means cluster counts

Run the standalone script from the repository root:

```powershell
python kmeans.py
```

It compares `k=1` through `k=10` on the `total_bill` and `size` features in `data/tips.csv`. Each run logs inertia to the local `mlflow.db`; runs with `k > 1` also log a silhouette score.

To browse the results:

```powershell
mlflow ui --backend-store-uri sqlite:///mlflow.db
```

Then open http://127.0.0.1:5000.

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
