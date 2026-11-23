# k-Means session: prompts, summary, and commentary

## Prompts (exact, in order)

1. > can you add a scree plot to the #k-Means.ipynb, read about them and wonder what it would look like, and if it matches the k used
2. > how about some loose python, k-means.py that puts uses mlflow to compare diff k's
3. > ooh explain diff of silhouette scoring versus train test split, does it have to do with supervised, versus unsupervised
4. > how about a k-Means-02.ipynb that does k means with penguin data, for learning, and how the clusters might match the species
5. > you are now in agent mode, go
6. > create a k-means-prompts.md file with my exact prompts, and a section short short summary of what you did, and maybe a commentary section, biggest lesson learned, or prompter is an id10t, b, b, blah...

## Summary

- Added a scree plot (inertia vs. `k`) to [k-Means.ipynb](./k-Means.ipynb), with commentary on whether the elbow matches the `k=6` already used in the notebook (spoiler: not really — elbow is closer to 3-4).
- Built [k-Means.py](./k-Means.py), a standalone script that sweeps `k=2..10`, logs params/metrics/plots per run to MLflow, and reports the best `k` by silhouette score.
- Explained why silhouette scoring (internal, label-free, no train/test split needed) is fundamentally different from supervised evaluation (needs held-out data + ground truth to catch overfitting).
- Built [k-Means-02.ipynb](./k-Means-02.ipynb): clusters penguin body measurements (scaled!) with `k=3`, then checks the clusters against the real `species` column using a crosstab and adjusted Rand index (≈0.80 — Gentoo separates cleanly, Adelie/Chinstrap overlap a bit), plus its own scree plot.
- Added `mlflow` as a project dependency (`uv add mlflow`) and a `.gitignore` for the local `mlflow.db`/`mlruns/` tracking artifacts it generates.

## Commentary

**Biggest lesson learned:** unsupervised learning doesn't give you a free "am I right?" check the way supervised learning does — you either borrow an internal geometric proxy (silhouette score) or, if you're lucky like with penguins, sneak in a real label afterward just to grade the homework. k-Means doesn't know what a species is; it just knows what's close to what.

**Runner-up lesson:** scaling matters more than it looks like it should. `body_mass_g` in the thousands next to `bill_depth_mm` in the tens means an unscaled k-Means run is basically just sorting penguins by weight and calling it clustering.

**Prompter self-assessment:** b, b, blah — honestly not bad for "loose python" and "ooh explain" energy. No notes, 10/10 vibes, occasionally skipped the part where you tell the agent it's allowed to actually touch files.
