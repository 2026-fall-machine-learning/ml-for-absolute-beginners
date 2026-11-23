"""Compare K-Means with different values of k using MLflow.

This is a plain Python script (not a notebook) that fits K-Means on the
tips dataset for a range of k values and logs each one as its own MLflow
run: the k used, the resulting inertia and silhouette score, and a plot
of the clusters. A final "summary" run logs the scree (elbow) plot
comparing all of the k values at once.

Run it with:
    uv run python kmeans_mlflow_compare.py

Then view the results with:
    uv run mlflow ui
and open http://127.0.0.1:5000 in your browser. The "kmeans-tips-k-comparison"
experiment lets you sort/compare runs by the `k` param and the `inertia` /
`silhouette_score` metrics, which is handy for picking a good k.
"""

import matplotlib.pyplot as plt
import mlflow
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

EXPERIMENT_NAME = "kmeans-tips-k-comparison"
FEATURES = ["total_bill", "size"]
K_VALUES = range(2, 11)  # silhouette score needs at least 2 clusters
RANDOM_STATE = 42


def load_data() -> pd.DataFrame:
    df = pd.read_csv("data/tips.csv")
    return df[FEATURES]


def plot_clusters(X: pd.DataFrame, model: KMeans, k: int) -> plt.Figure:
    """Scatter plot of the data colored by cluster, with centroids marked."""
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.scatter(X[FEATURES[0]], X[FEATURES[1]], c=model.labels_, cmap="rainbow", s=50)
    ax.scatter(
        model.cluster_centers_[:, 0],
        model.cluster_centers_[:, 1],
        c="black",
        s=200,
        alpha=1,
        label="centroids",
    )
    ax.set_xlabel(FEATURES[0])
    ax.set_ylabel(FEATURES[1])
    ax.set_title(f"K-Means clusters (k={k})")
    ax.legend()
    return fig


def plot_scree(k_values: list[int], inertias: list[float]) -> plt.Figure:
    """Inertia vs. k, the scree/elbow plot, for comparing all runs at once."""
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(list(k_values), inertias, marker="o")
    ax.set_xlabel("Number of clusters (k)")
    ax.set_ylabel("Inertia")
    ax.set_title("Scree plot across MLflow runs")
    ax.set_xticks(list(k_values))
    return fig


def main() -> None:
    mlflow.set_experiment(EXPERIMENT_NAME)

    X = load_data()
    inertias = []

    for k in K_VALUES:
        with mlflow.start_run(run_name=f"k={k}"):
            model = KMeans(n_clusters=k, n_init="auto", random_state=RANDOM_STATE)
            model.fit(X)

            inertia = model.inertia_
            silhouette = silhouette_score(X, model.labels_)
            inertias.append(inertia)

            mlflow.log_param("k", k)
            mlflow.log_param("features", FEATURES)
            mlflow.log_metric("inertia", inertia)
            mlflow.log_metric("silhouette_score", silhouette)

            fig = plot_clusters(X, model, k)
            mlflow.log_figure(fig, f"clusters_k{k}.png")
            plt.close(fig)

            print(f"k={k:>2}  inertia={inertia:,.1f}  silhouette={silhouette:.3f}")

    # Log the scree plot (and the raw numbers) in their own summary run so
    # it's easy to find alongside the per-k runs above.
    with mlflow.start_run(run_name="summary"):
        fig = plot_scree(list(K_VALUES), inertias)
        mlflow.log_figure(fig, "scree_plot.png")
        plt.close(fig)
        for k, inertia in zip(K_VALUES, inertias):
            mlflow.log_metric("inertia_by_k", inertia, step=k)

    print("\nDone! Run `uv run mlflow ui` and open http://127.0.0.1:5000 to compare runs.")


if __name__ == "__main__":
    main()
