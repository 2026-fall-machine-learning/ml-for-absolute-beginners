# Learning K-Means Clustering

## My prompts (exact words)

1. can you add a scree plot to the k-means.ipynb, i read about them and wonder what they might look like with this data, and if k=6 is right
2. how about spome loose python that uses mlflow to compare different k values?
3. create k-means-02.ipynb with penguin data, so k = 3 since we have three species in the data, and show how cluster match species
4. drop all my prompts in a learning-k-means-clustering.md file, exact words, and summarize what you taught me

## What was covered

### 1. Scree (elbow) plots for choosing k
- Added a scree/elbow plot to `k-Means.ipynb` (tips data): fit `KMeans` for `k = 1` to `10`, collected `inertia_` (sum of squared distances from points to their assigned centroid) for each, and plotted inertia vs. `k`.
- **Inertia always decreases as `k` increases** - the question is where the improvement stops being worth it. The "elbow" (where the curve bends and flattens) is a rule-of-thumb for picking `k`.
- For the tips data, the elbow landed closer to `k = 4`-`5` rather than `k = 6`. `k = 6` wasn't wrong (it's past the steep part of the curve), but it's not the sharpest elbow either - a reminder that the scree plot is a guide, not a guarantee, and domain knowledge about what the clusters should represent still matters.

### 2. Comparing k values with MLflow
- Wrote `kmeans_mlflow_compare.py`, a standalone (non-notebook) script that loops over `k = 2..10`, fits `KMeans` for each, and logs an MLflow run per `k` with:
  - the `k` parameter,
  - `inertia` and `silhouette_score` metrics,
  - a cluster scatter plot artifact.
- Logged a summary run with the full scree plot so it's easy to find alongside the individual runs.
- Added `mlflow` as a project dependency and a `.gitignore` so the generated `mlruns/`/`mlflow.db` tracking data and `.venv/` don't get committed.
- Ran it and used `mlflow ui` to confirm results are browsable/comparable; noted that **silhouette score and inertia can disagree** (silhouette peaked at `k = 2` here even though inertia kept dropping), which is a good illustration of why no single metric picks `k` for you.

### 3. K-Means vs. known labels (penguins)
- Built `k-means-02.ipynb` using the `penguins` dataset, which has 3 known species (Adelie, Chinstrap, Gentoo) - a nice case for testing whether unsupervised clustering recovers a label it never saw.
- Dropped rows with missing measurements, then clustered on 4 numeric features (`bill_length_mm`, `bill_depth_mm`, `flipper_length_mm`, `body_mass_g`) with `k = 3`.
- **Feature scaling matters**: `StandardScaler` was used because `body_mass_g` (thousands) would otherwise dominate the distance calculation over `bill_depth_mm` (tens), making K-Means effectively ignore the smaller-scale features.
- Compared clusters to species with a `pd.crosstab` plus two scoring methods:
  - **Purity**: fraction of points matching their cluster's majority species (91.9% here).
  - **Adjusted Rand Index (ARI)**: a chance-corrected agreement score, 1.0 = perfect match, 0.0 = random (0.799 here).
- Visualized cluster assignment vs. true species side-by-side on a scatter plot. Result: Gentoo penguins (notably larger, longer flippers) were separated almost perfectly, while Adelie and Chinstrap overlapped more and were sometimes confused with each other - illustrating that K-Means finds round, evenly-sized groups based on distance, which won't always line up exactly with human-defined categories.
