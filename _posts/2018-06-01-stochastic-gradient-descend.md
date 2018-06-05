---
type: post
title: "Stochastic Gradient Descend"
date: 2018-06-01
---

Summarized from [here](https://www.quora.com/What-is-an-intuitive-explanation-of-stochastic-gradient-descent).

## What gradient descend is

Iterative algorithm to to find the minimum of a function.
Commonly used to minimize the error of an ML algorithm.

Makes an initial guess at best parameters for a model,
then keeps iterating towards the ideal solution until the parameters are "good enough".

## How it works

Given a dataset on real estate prices, with the goal of creating a model
to predict the price of a new house, one could model the rent price using a linear model,
where `y` is the price of the house and `x` is the number of rooms in the house.

To find the parameters `m` and `c` of the model `y = mx + c`.

### Batch gradient descend

1. Pick an estimate of `m` and `c`.
2. Use that estimate to predict the rent prices of all your data instances.
3. Find the mean error.
4. If the error is too high, adjust `m` and `c` and goto step 2.


### Stochastic gradient descend

1. Pick an estimate of `m` and `c`.
2. Use that estimate to predict the rent prices of one test instance.
3. Find the mean error.
4. If the error is too high, adjust `m` and `c` and goto step 2.


## Comparing the two

* # adjustments needed: stocastic > batch
* Dataset size: use stocastic on large datasets, batch on smaller datasets.
* Its easier to parallalize batch datasets as you need to get feedback
  from one small iteration to another.
* Batch gradient descend minimizes the error better than Stochastic,
  but stochastic converges much faster for large datasets.
* In practice stochastic gradient descend is recommended as it usually does a
  good enough job and is more efficient.





