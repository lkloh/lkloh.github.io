---
type: post
title: "Bias-Variance tradeoff"
date: 2018-05-13
---

## What it is

When training a ML model, there are many different algorithms to use.
E.g. regressions, decision trees, neural networks, SVM.

The algorithms differ in the amount of bias vs variance.

## Bias

Occurs when an ML algorithm has limited flexibility to learn the true signal from a dataset.

High bias, low variance:
Model is very consistent (e.g. get the same prediction for some value
after being trained by different datasets),
but inaccurate on average.

Using biased but simple algorithms may underfit models,
that cannot learn signal from the data.

## Variance

An ML algorithm's sensitivity to specific sets of training data.

High Variance - low bias.
Model is more accurate on average when variance is high,
but inconsistent when making individual predictions.

Using accurate but complex algorithms may overfit the data,
as they memorize the noise instead of the signal.

## Why the tradeoff

Low variance algorithms tend to be less complex.
For example, parametric models such as linear models.

Low bias algorithms tend to be more complex.
For example, non-parametric algorithms like decision trees,
which rely on information about the data to make predictions.

## How to balance between bias and accuracy

Minimize total error.

```
total error = bias^2 + variance + irreducible error
```

Irreducible error is noise that can sometimes be reduced
by data cleaning, but cannot be reduced by the algorithms.





