---
type: post
title: "Preventing model overfitting"
date: 2018-06-07
---

Summarized from [here](https://elitedatascience.com/overfitting-in-machine-learning).

## When is a model overfitted?

When it does much better on the training dataset than testing dataset.


## Preventing overfitting

### Occam's razor test

Start with a simple model. 
Try more complex models.
Check to see if the additional complexity is worth it.

### Cross-validation

Split the dataset into multiple train-test sets,
and use them to adjust the model.

### Add more data

Usually helps detect the signal better,
assuming the additional data isn't exceptionally noisy.

### Remove features

Remove irrelevant input features.
You need to be able to explain how each feature fits into the story.
If you can't remove the feature.

### Early stopping

When training a model iteratively,
early iterations provide bigger performance gains than late iterations,
which can cause overfitting.

### Regularization

Techniques to simplify the model.
Perhaps by pruning a decision tree, etc.

### Ensembling

Combining predictions from separate models.
Example: Bagging multiple compelx models to smooth out their predictions.








