# Decision Tree notebook — session notes

## Prompt 1
> why decision tree notebook diff mean error when has random_state and not shuffle, should i expect same same each run

Checked `train_test_split` — it had `random_state=42` set (with `shuffle=True` commented out, which is fine since `shuffle=True` is the default). Found the real issue: `DecisionTreeRegressor()` was created with no `random_state`, so the tree's internal random feature permutation/tie-breaking varied each run, changing the tree structure and the error metric.

## Prompt 2
> think i did that, but not same same

Looked at the updated cell — `random_state=42` had also been commented out in `train_test_split`. So both the split *and* the model were unseeded, meaning a different train/test split every run on top of the model randomness. Recommended uncommenting `random_state=42` in the split while keeping it on the model.

## Prompt 3
> does the cross_val_score stuff i added make sense, take random_state out of split but leave in model, or am i an id10t

Confirmed this was fine, not a mistake — `cross_val_score(model2, X, y, cv=5)` uses the full `X, y` and does its own internal KFold splitting (deterministic by default, non-shuffled), so it doesn't touch `train_test_split` at all. Keeping `random_state=42` on the model is correct and sufficient here. Also flagged that the returned scores are R², and the wide/negative spread across folds (mean ≈ 0.008) pointed to an unconstrained tree overfitting.

## Prompt 4
> should we always run cross_val_score, hmm

Explained no — CV is best for small/medium datasets and model/hyperparameter comparison, but overkill for large datasets or quick iteration, and shouldn't replace a final untouched holdout test set for the final reported number. Also noted plain KFold CV isn't valid for time-series/grouped data.

## Prompt 5
> just for my understanding, yeah right, random_state needed on dt model since the model itself randomizes internally, so random_state there and on split, makes it repeatable

Confirmed: two independent randomness sources (split row-selection vs. tree's internal split-tie-breaking), each needs its own seed; fixing only one doesn't fix the other.

## Prompt 6
> but could be seeded with diff numbers , not both 42

Confirmed: the two `random_state` values are independent RNGs, not linked — e.g. `random_state=7` on the split and `random_state=99` on the model is equally reproducible. Using `42` for both is just convention, not a requirement.
