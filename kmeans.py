from pathlib import Path

import mlflow
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score


ROOT = Path(__file__).resolve().parent
DATA_PATH = ROOT / "data" / "tips.csv"
FEATURES = ["total_bill", "size"]
K_VALUES = range(1, 11)


def main() -> None:
    data = pd.read_csv(DATA_PATH)
    X = data[FEATURES]

    mlflow.set_tracking_uri(f"sqlite:///{ROOT / 'mlflow.db'}")
    mlflow.set_experiment("K-means k comparison")

    for k in K_VALUES:
        model = KMeans(n_clusters=k, random_state=42, n_init=10)
        labels = model.fit_predict(X)

        with mlflow.start_run(run_name=f"k={k}"):
            mlflow.log_params({"k": k, "random_state": 42, "n_init": 10})
            mlflow.log_metric("inertia", model.inertia_)

            if k > 1:
                score = silhouette_score(X, labels)
                mlflow.log_metric("silhouette_score", score)
                print(f"k={k}: inertia={model.inertia_:.2f}, silhouette={score:.3f}")
            else:
                print(f"k={k}: inertia={model.inertia_:.2f}")


if __name__ == "__main__":
    main()
