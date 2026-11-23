# Learning k-Means Clustering

## My prompts (exact words)

1. can you add a scree plot to the #k-Means.ipynb, i read about them and wonder what it might look like with this data, and whether k = 6 i right
2. how about some loose pythong k-means.py that uses mlflow to compare different k values
3. what what, silhouette score, neve seen it, is it scoring unsupervised versus supervised, ah, there is no train test split, make me smart
4. create k-means-02.ipynb with penguin data, so k = 3 since we have 3 species in the data, and show how clusters match species
5. oops, you are now an agent, go getm 007
6. drop all my prompts in a learing-k-means-clustering.md file, exact words, and summarize what you taught me

## Summary of what was covered

### 1. Scree plots for choosing k
Added a scree plot to `k-Means.ipynb` that fits `KMeans` for `k = 1..10` on the tips dataset (`total_bill`, `size`) and plots `k` vs. `inertia_` (within-cluster sum of squared distances). Inertia always drops as `k` increases, so the goal is to find the "elbow" where the drop-off slows down. For this data, the elbow looked more like `k = 4` or `5` than `k = 6` -- `k = 6` is past the steepest drop but not a uniquely obvious choice, since the curve flattens gradually rather than sharply.

### 2. Comparing k values with MLflow
Built `k-means.py`, a standalone script that loops over `k = 2..10`, fits `KMeans` on the same features, and logs each run to MLflow: the `k` parameter, `inertia` and `silhouette_score` metrics, the fitted model, and a cluster scatter plot artifact. Running `mlflow ui` lets you sort and compare runs side by side instead of eyeballing a single plot. Added `mlflow` to `pyproject.toml` and a `.gitignore` for the local `mlflow.db`/`mlruns/` tracking artifacts.

### 3. What silhouette score is (and why there's no train/test split)
- **Silhouette score** measures clustering quality without ground-truth labels. For each point it compares *a* (average distance to points in its own cluster) and *b* (average distance to points in the nearest other cluster): $s = \frac{b-a}{\max(a,b)}$. Values near +1 mean a point sits comfortably in its own cluster; near 0 means it's on a border; negative means it's probably in the wrong cluster. Averaging over all points gives one score for the whole clustering -- higher is better.
- **Unsupervised, not supervised**: silhouette score never looks at true labels -- it only uses the geometry/distances of the data and the cluster assignments produced. This contrasts with supervised metrics (accuracy, F1, RMSE) that require a ground-truth `y`.
- **Why no train/test split**: supervised learning tests whether a model generalizes to predict a label it hasn't seen, which requires held-out data. k-Means isn't predicting an independently-existing label -- it's partitioning data by proximity, so there's no "correct answer" in a held-out set to check against. (Train/test-style splitting can still show up for checking cluster *stability*, or when using `.predict()` to assign new unseen points to existing centroids -- but that's different from label-accuracy evaluation.)

### 4. Clustering real species: the penguins notebook
Built `k-means-02.ipynb` using the existing `data/penguins.csv`, which (unlike tips.csv) has a real ground-truth label: `species` (Adelie, Chinstrap, Gentoo). Since there really are 3 species, `k = 3` is justified rather than guessed. Key points demonstrated:
- Clustered on all four body measurements (`bill_length_mm`, `bill_depth_mm`, `flipper_length_mm`, `body_mass_g`).
- **Scaling matters**: `body_mass_g` is in the thousands while bill measurements are in the tens, so without `StandardScaler`, body mass would dominate k-Means' distance calculations. Scaled features gave a 91.9% cluster-to-species match rate vs. only 67.9% unscaled -- a concrete illustration of why feature scaling matters for distance-based algorithms.
- Since k-Means' cluster numbers (0, 1, 2) are arbitrary, matching them to species requires a crosstab plus mapping each cluster to its majority species after the fact -- reinforcing that this check is a sanity check, not something the algorithm optimizes for, since it never saw the labels during fitting.
