# K-means Penguins Chat Transcript

## User

Create k-means-02.ipynb with penguin data, so k = 3 since we have 3 species in the data and show how clusters match species

## Assistant

Created `k-means-02.ipynb` with:

- Penguin data loaded from `data/penguins.csv`
- Missing measurements removed
- Numeric body measurements standardized
- K-means configured with `k = 3`
- A cluster/species cross-tabulation
- Majority-match accuracy and Adjusted Rand score
- Side-by-side plots comparing actual species with predicted clusters

Verified the notebook code against the local dataset. The run produced:

- 342 penguins used
- Silhouette score: 0.447
- Majority-match accuracy: 91.52%
- Adjusted Rand score: 0.793

## User

Drop the chat transcript somewhere in a transcripts directory in this repo.

## Assistant

Saved this conversation transcript in `transcripts/kmeans-penguins.md`.
