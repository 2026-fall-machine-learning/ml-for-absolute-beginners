# logreg-playing.md

## Original Prompts

can you summarize in human readable table this confusion matrix from this code snippet

[[44  1  0]
 [ 0 23  0]
 [ 0  0 32]]

print(confusion_matrix(y_test, model_test))

---

increased max_iter, 100 to 1000 and now this, why

[[43  2  0]
 [ 0 23  0]
 [ 0  0 32]]

---

so random_state preserves run randomness for consistency, not setting it, get diff results based on train test splits, hmm, how does one handle this in real world

---

import for cross_val_score

---

got this when calling cros_val_score

ConvergenceWarning: lbfgs failed to converge after 100 iteration(s) (status=1):
STOP: TOTAL NO. OF ITERATIONS REACHED LIMIT

Increase the number of iterations to improve the convergence (max_iter=100).

---

interpret

model2 = LogisticRegression(max_iter=10000)

scores = cross_val_score(model2, X, y, cv=5)

print(scores)
print(scores.mean())

[1.         0.98507463 0.98507463 1.         1.        ]
0.9940298507462686

---

one sentence def of cross validation and why pros use instead of random_state, if they do, or i could be wrong, or mlflow with hyperparameter experiments, or i may be messing about with unrelated concepts

---

hmm, maybe running a notebook example to see these moving parts is my lecture demo today, rather than textbook tldr on knn, save that for future week, follow up on logreg, dt, and forest work and these concepts, hmm, idiot or genius

---

cross validation one line explanation to test me

---

one more explanation of this confusion matrix, 3 classes, so note simple false pos/neg, tru pos/neg

[[49  0  1]
 [ 2 17  0]
 [ 0  0 31]]

---

max_iter-10000, no failed predictions, expected, or overfitt

## Brief Summary of Concepts Explored

### Confusion Matrices

Started with interpreting multiclass confusion matrices.

Key takeaway:

- Rows = actual class
- Columns = predicted class
- Diagonal values are correct predictions
- Off-diagonal values are mistakes

### max_iter

Explored increasing:

```python
LogisticRegression(max_iter=100)
```

to

```python
LogisticRegression(max_iter=1000)
```

and later

```python
LogisticRegression(max_iter=10000)
```

Key takeaway:

- More iterations does not automatically mean better accuracy.
- max_iter gives the optimizer more time to converge.
- Logistic regression becomes more optimized, not necessarily more accurate on unseen data.

### Convergence Warning

Observed:

```text
lbfgs failed to converge
STOP: TOTAL NO. OF ITERATIONS REACHED LIMIT
```

Key takeaway:

- Model training did not finish optimization.
- Increase max_iter and/or scale data.
- Warning does not mean model failed.

### random_state

Discussed:

```python
train_test_split(..., random_state=42)
```

Key takeaway:

- random_state makes randomness repeatable.
- Useful for fair comparisons.
- Does not improve the model.
- Improves reproducibility.

### Cross Validation

Used:

```python
from sklearn.model_selection import cross_val_score
```

and

```python
scores = cross_val_score(model, X, y, cv=5)
```

Key takeaway:

- Cross-validation evaluates a model on multiple train/test splits.
- Produces a more trustworthy estimate than one split.

One-line definition:

> Cross-validation tests a model on multiple train/test splits to get a more reliable estimate of performance.

### Results

```python
[1.0, 0.985, 0.985, 1.0, 1.0]
Mean = 0.994
```

Interpretation:

- Average accuracy ≈ 99.4%
- Performance is very stable across folds.
- Strong evidence of generalization.

### Overfitting Discussion

Observed a perfect test score after increasing max_iter.

Key takeaway:

- Perfect accuracy alone does not indicate overfitting.
- Logistic regression is a relatively simple model.
- Strong cross-validation results argue against severe overfitting.

### MLflow Connection

Connected concepts:

```text
Hyperparameters
    ↓
Cross Validation
    ↓
Mean Score
    ↓
MLflow Tracking
    ↓
Compare Experiments
```

Key takeaway:

- random_state = reproducibility
- cross-validation = evaluation
- hyperparameters = tuning
- MLflow = experiment tracking

### Potential Lecture Flow

1. Train logistic regression.
2. Evaluate accuracy.
3. Inspect confusion matrix.
4. Change max_iter.
5. Observe changed results.
6. Discuss convergence warnings.
7. Introduce random_state.
8. Explain train/test splits.
9. Introduce cross-validation.
10. Compare single-score vs average-score evaluation.
11. Revisit MLflow experiment tracking.

Potential theme:

> Don't trust the first accuracy number you see.