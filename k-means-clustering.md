# k-Means Clustering - My Prompts & What I Learned

## My prompts (exact words)

1. can you add a scree plot to the #k-Means.ipynb, i read about them and wonder what it might look like with this data, and whether k = 6 is right

2. how about some loose python k-means.py that uses mlflow to compare different k values

3. silhouette score, never seen it, is it scoring unsupervised versus supervised, there is no train test split, make me smart

4. create k-means-02.ipynb with penguin data, so k = 3 since we have 3 species in the data, and show how clusters match species

5. put all my prompts in a k-means-clustering.md file, exact words, and summarize what you taught me

## Summary of what I learned

### Scree (elbow) plots for choosing k
- A scree plot plots **inertia** (sum of squared distances from each point to its assigned centroid) against `k`.
- Inertia always decreases as `k` grows, so the curve always slopes down - there's no single "correct" stopping point, just diminishing returns.
- The "elbow" (where the curve bends and flattens) is a rule-of-thumb candidate for `k`, not a guarantee.
- On the tips dataset (`total_bill`, `size`), inertia dropped sharply through about `k = 4` then flattened more gradually, suggesting the elbow is closer to `k = 3-4` than the notebook's `k = 6` - `k = 6` still "works," it's just splitting the data more finely than the elbow alone would suggest.

### Tracking experiments with MLflow
- Built `k-means.py`, a standalone script that fits k-Means for a range of `k` values and logs each run to MLflow (params, metrics, plots) so runs can be compared side by side instead of eyeballing one plot.
- Added `mlflow` as a project dependency via `uv add mlflow`.
- MLflow's local tracking store defaults to a SQLite file (`mlflow.db`) for run metadata, plus an `mlruns/` folder for artifact files (plots, etc.) - both are generated/local and were added to `.gitignore`.
- Workflow: `uv run python k-means.py` to generate runs, then `uv run mlflow ui` to open a browser UI and compare `k` values by inertia, silhouette score, and cluster plots.

### Silhouette score - unsupervised, not supervised
- Silhouette score is a **purely unsupervised** metric - no labels, no train/test split needed, because there's no ground truth to check predictions against in clustering.
- For each point `i`: `a(i)` = average distance to other points in its own cluster (tightness), `b(i)` = average distance to points in the nearest other cluster (separation).
- Score per point: `s(i) = (b(i) - a(i)) / max(a(i), b(i))`, averaged over all points for the reported number. Range is -1 to 1:
  - close to +1: well-clustered (tight and well-separated)
  - close to 0: on the border between two clusters
  - negative: probably assigned to the wrong cluster
- It answers "do these clusters look like real, separated groups?" rather than "did we predict the right answer?" - that's why it only needs the data and the cluster labels the model produced.
- Caveat: silhouette tends to favor fewer, larger, well-separated clusters, since the "distance to nearest other cluster" term shrinks once many clusters are packed into the same space. On the tips data it peaked at `k = 2`, disagreeing with the scree plot's suggestion of `k = 3-4` - a good reminder that different metrics can disagree, and that's informative rather than a bug.

### Validating k-Means against known labels (penguins)
- Built `k-means-02.ipynb`, clustering the penguins dataset (`bill_length_mm`, `bill_depth_mm`, `flipper_length_mm`, `body_mass_g`) with `k = 3`, chosen because we independently know there are 3 species.
- Standardized features first (`StandardScaler`) since `body_mass_g` (thousands) would otherwise dominate distance calculations over `bill_depth_mm` (tens) purely due to units.
- Cluster numbers (0/1/2) are arbitrary and have no inherent meaning, so comparing clusters to species requires matching each cluster to its most common species first (via `pd.crosstab` + `idxmax`).
- Used the **Adjusted Rand Index (ARI)** to score agreement between two groupings (clusters vs. true species) in a way that's immune to label numbering and corrected for chance; 0 = random, 1 = perfect.
- Result: 91.9% matched accuracy, ARI of 0.799. Gentoo was recovered perfectly (distinct flipper length); nearly all confusion was between Adelie and Chinstrap, which overlap more on the two plotted measurements and are mainly separated by `bill_depth_mm` instead - a concrete demonstration that unsupervised clustering can recover real structure when the features are genuinely informative.
