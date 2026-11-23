"""Compare k-Means clustering across different values of k, tracked with MLflow.

For each candidate k, this fits a KMeans model on the tips dataset, logs the
parameter, metrics (inertia and silhouette score), and the fitted cluster
scatter plot as an MLflow artifact. It also logs one extra "summary" run
containing the scree plot (inertia vs. k) across all candidates, mirroring the
elbow-method analysis from k-Means.ipynb.

Run it with:
    uv run k-Means.py

Then inspect results with:
    uv run mlflow ui
"""

import matplotlib.pyplot as plt
import mlflow
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

K_VALUES = range(2, 11)  # silhouette score needs at least 2 clusters
FEATURES = ["total_bill", "size"]
USED_K = 6  # the k chosen in k-Means.ipynb, for comparison


def load_data() -> pd.DataFrame:
    df = pd.read_csv("data/tips.csv")
    return df[FEATURES]


def plot_clusters(X: pd.DataFrame, labels, centroids, k: int) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.scatter(X[FEATURES[0]], X[FEATURES[1]], c=labels, cmap="rainbow", s=50)
    ax.scatter(centroids[:, 0], centroids[:, 1], c="black", s=200, alpha=1)
    ax.set_xlabel(FEATURES[0])
    ax.set_ylabel(FEATURES[1])
    ax.set_title(f"k-Means clusters (k={k})")
    return fig


def plot_scree(k_values, inertias) -> plt.Figure:
    fig, ax = plt.subplots(figsize=(6, 5))
    ax.plot(list(k_values), inertias, marker="o")
    ax.axvline(x=USED_K, color="red", linestyle="--", label=f"k={USED_K} (notebook)")
    ax.set_xlabel("Number of clusters (k)")
    ax.set_ylabel("Inertia")
    ax.set_title("Scree plot across runs")
    ax.legend()
    return fig


def main() -> None:
    mlflow.set_experiment("k-means-tips")
    X = load_data()

    inertias = []
    silhouettes = []
    with mlflow.start_run(run_name="k-sweep-summary"):
        for k in K_VALUES:
            with mlflow.start_run(run_name=f"k={k}", nested=True):
                model = KMeans(n_clusters=k, n_init=10, random_state=42)
                labels = model.fit_predict(X)

                inertia = model.inertia_
                silhouette = silhouette_score(X, labels)
                inertias.append(inertia)
                silhouettes.append(silhouette)

                mlflow.log_param("k", k)
                mlflow.log_metric("inertia", inertia)
                mlflow.log_metric("silhouette_score", silhouette)

                fig = plot_clusters(X, labels, model.cluster_centers_, k)
                mlflow.log_figure(fig, f"clusters_k{k}.png")
                plt.close(fig)

                print(f"k={k:2d}  inertia={inertia:10.1f}  silhouette={silhouette:.3f}")

        # Pick the k with the highest silhouette score across the sweep.
        best_k_by_silhouette = list(K_VALUES)[silhouettes.index(max(silhouettes))]

        mlflow.log_metric("best_k_by_silhouette", best_k_by_silhouette)
        mlflow.log_param("k_values_tested", list(K_VALUES))

        scree_fig = plot_scree(K_VALUES, inertias)
        mlflow.log_figure(scree_fig, "scree_plot.png")
        plt.close(scree_fig)

        print(f"\nBest k by silhouette score: {best_k_by_silhouette}")
        print(f"k used in k-Means.ipynb: {USED_K}")


if __name__ == "__main__":
    main()
