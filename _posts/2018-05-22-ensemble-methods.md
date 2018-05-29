---
type: post
title: "Ensemble methods"
date: 2018-05-22
---

[Summarized from here](https://www.toptal.com/machine-learning/ensemble-methods-machine-learning).

## What is is

Creating multiple models and combining them to improve results.
Usually does better than any one model 
- for example the winner of the Netflix Competition used an ensemble method.

## Voting ensemble method

One of the easiest - used for classification.

1. Create multiple classification models using some training dataset and create predictions.
2. Vote

  Majority voting - every model predicts (votes) for each test instance,
  and the one with over 50% of votes wins.
  If there is no majority concensus, the ensemble method cannot make a stable prediction for that instance.
  You could still use the one getting the most votes.

  Weighted voting - Some models are more important than others. Similar to majority voting
  but you also need to come up with a set of weights that make sense.

## Average ensemble method

Also easy - used for regression models

1. Create multiple classification models using some training dataset and create predictions.
2. Average

Simple average - average every prediction for each test instance,
to reduce overfit and noise.

Weighted average - multiply each prediction of a model by a weight and find the average.
Again you must come up with a set of weights.












