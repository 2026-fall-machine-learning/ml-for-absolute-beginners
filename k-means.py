"""Compare k-Means clustering across several values of k, tracked with MLflow.

For each candidate k, this fits a KMeans model on the tips dataset
(total_bill, size), logs the parameter and resulting metrics (inertia and
silhouette score) to MLflow, and saves the cluster scatter plot as an
artifact. Open the MLflow UI afterwards to compare runs side by side:

    uv run mlflow ui

Then browse to http://127.0.0.1:5000 and look at the "k-means-tips"
experiment.
"""

import matplotlib.pyplot as plt
import mlflow
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

K_VALUES = range(2, 11)  # silhouette score needs at least 2 clusters
FEATURES = ["total_bill", "size"]


def load_data() -> pd.DataFrame:
    df = pd.read_csv("data/tips.csv")
    return df[FEATURES]


def run_for_k(X: pd.DataFrame, k: int) -> None:
    with mlflow.start_run(run_name=f"k={k}"):
        model = KMeans(n_clusters=k, n_init="auto", random_state=42)
        labels = model.fit_predict(X)

        inertia = model.inertia_
        silhouette = silhouette_score(X, labels)

        mlflow.log_param("k", k)
        mlflow.log_metric("inertia", inertia)
        mlflow.log_metric("silhouette_score", silhouette)
        mlflow.sklearn.log_model(model, name="model")

        fig, ax = plt.subplots(figsize=(6, 4))
        scatter = ax.scatter(X["total_bill"], X["size"], c=labels, cmap="rainbow", s=40)
        ax.scatter(
            model.cluster_centers_[:, 0],
            model.cluster_centers_[:, 1],
            c="black",
            s=150,
            marker="X",
            label="centroids",
        )
        ax.set_xlabel("total_bill")
        ax.set_ylabel("size")
        ax.set_title(f"k-Means clusters (k={k})")
        ax.legend()
        mlflow.log_figure(fig, "clusters.png")
        plt.close(fig)

        print(f"k={k:2d}  inertia={inertia:10.2f}  silhouette={silhouette:.4f}")


def main() -> None:
    X = load_data()
    mlflow.set_experiment("k-means-tips")

    for k in K_VALUES:
        run_for_k(X, k)


if __name__ == "__main__":
    main()
