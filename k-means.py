"""Compare k-Means clustering for several values of k, tracked with MLflow.

This is a plain Python counterpart to k-Means.ipynb. Instead of eyeballing a
single scree plot, it fits KMeans for a range of k values and logs each run
(parameters, metrics, and plots) to MLflow so the runs can be compared side
by side in the MLflow UI.

Run it with:
    uv run python k-means.py

Then view the results with:
    uv run mlflow ui
and open the printed local URL (typically http://127.0.0.1:5000).
"""

import matplotlib.pyplot as plt
import mlflow
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

K_VALUES = range(2, 11)  # silhouette score needs at least 2 clusters
FEATURES = ["total_bill", "size"]
EXPERIMENT_NAME = "kmeans-tips"


def load_data() -> pd.DataFrame:
    df = pd.read_csv("data/tips.csv")
    return df[FEATURES]


def plot_clusters(X: pd.DataFrame, model: KMeans) -> plt.Figure:
    """Scatter plot of the data colored by cluster, with centroids marked."""
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.scatter(X["total_bill"], X["size"], c=model.labels_, cmap="rainbow", s=50)
    ax.scatter(
        model.cluster_centers_[:, 0],
        model.cluster_centers_[:, 1],
        c="black",
        s=200,
        alpha=1,
    )
    ax.set_xlabel("total_bill")
    ax.set_ylabel("size")
    ax.set_title(f"k-Means clusters (k={model.n_clusters})")
    return fig


def plot_scree(k_values: range, inertias: list[float]) -> plt.Figure:
    """Elbow/scree plot: inertia vs. number of clusters."""
    fig, ax = plt.subplots(figsize=(7, 5))
    ax.plot(list(k_values), inertias, marker="o")
    ax.set_xlabel("Number of clusters (k)")
    ax.set_ylabel("Inertia")
    ax.set_title("Scree plot for k-Means")
    ax.set_xticks(list(k_values))
    return fig


def main() -> None:
    X = load_data()
    mlflow.set_experiment(EXPERIMENT_NAME)

    inertias = []

    for k in K_VALUES:
        with mlflow.start_run(run_name=f"k={k}"):
            model = KMeans(n_clusters=k, n_init=10, random_state=42)
            model.fit(X)

            inertia = model.inertia_
            inertias.append(inertia)
            score = silhouette_score(X, model.labels_)

            mlflow.log_param("k", k)
            mlflow.log_metric("inertia", inertia)
            mlflow.log_metric("silhouette_score", score)

            fig = plot_clusters(X, model)
            mlflow.log_figure(fig, f"clusters_k{k}.png")
            plt.close(fig)

            print(f"k={k:>2}  inertia={inertia:,.1f}  silhouette={score:.3f}")

    # Log the scree plot once, outside the per-k runs, so it's easy to find.
    with mlflow.start_run(run_name="scree-plot-summary"):
        for k, inertia in zip(K_VALUES, inertias):
            mlflow.log_metric("inertia", inertia, step=k)
        fig = plot_scree(K_VALUES, inertias)
        mlflow.log_figure(fig, "scree_plot.png")
        plt.close(fig)

    print("\nDone. Run `uv run mlflow ui` and open the printed URL to compare runs.")


if __name__ == "__main__":
    main()
