---
type: post
title: "Sampling and splitting data"
date: 2018-06-06
---

## When splitting data should happen

Before modeling the data, split into training and test sets.

Use about 20% of data for testing, 80% for training.


## Cross-validation

### What it is used for

Estimate the performance of a method to build a model.

### How it works

Train and evaluate a model multiple times using the same mthod.

### Steps

```
Split the data into `k` equal parts "folds", where `k=10` is the default.
for i in k:
  Train the model on the [1,...,i-1,i+1,...,k]-th folds.
  Evaluate the model on the i-th fold
Aggregate performance across all k folds to get the performance metric.
```

