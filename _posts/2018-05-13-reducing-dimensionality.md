---
type: post
title: "Reducing dimensionality"
date: 2018-05-13
---

Summarized from [here](https://elitedatascience.com/dimensionality-reduction-algorithms).

## Dimensionality

The number of features (input variables) in a dataset.

* Many features: some algorithms cannot train effective models.
  Such as clustering algorithms that use distance calculations.

## High-dimensionality makes it hard to search through a space.

1D: O(n) time

2D: O(n^2) time

3D: O(n^3) time

...

XD: O(n^x) time

## Reducing dimensionality by feature selection

Remove irrelevant/redundant features from the dataset before using it
to train a model.

Models with built-in feature selection: regularized regression/ random forest.

Feature sepection can be supervised or unsupervised.

## Reducing dimensionality by variance thresholds

If the value of a features has low variance below a threshold, remove it.
For example, if 98% of a health dataset's participants are men,
then remove the feature for "gender" as it doesn't tell you much.

Variance is dependent on scale, so normalize the features first.

## Reducing dimensionality by correlation thresholds

Remove features that are high correlated with others (very similar features),
to remove redundant information.

For example, given a financial dataset with a feature called
"Money in USD" and another called "Money in Euros",
you can remove one of them.

Unfortunately you also need to decide on a correlation threshold,
which is hard to pick. You must balance between dropping useful information
and pruning redundant information.

## Reducing dimensionality by supervised feature selection

Genetic algorithms can help. 
"Genes" are features and "organisms" are a candidate set of features.
Keep pruning the organisms until the population of organisms converge.
Commonly used for very high dimensionality datasets when its not possible
to do an exhaustive search.
Drawback is that the algorithms can get pretty complex.

