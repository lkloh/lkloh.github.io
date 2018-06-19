---
type: post
title: "L1 vs L2 regularization"
date: 2018-06-13
---

[This paper](https://icml.cc/imls/conferences/2004/proceedings/papers/354.pdf)
studies the use of regularization methods to prevent overfitting during supervised learning.
Overfitting can occur when there are many irrelevant features.
The more features there are, the more number of training examples needed for
an algorithm to learn well.

Regularization is useful to make the parameters small to prevent overfitting
when the training set size is small relative to the number of features.


## Best case: L1 regularization causes #training examples needed to grow proportionally to O(log(#irrelevant features))

L1 regularization encourages the sum of the absolute values of parameters to be small,
causing many parameters to be 0.
Thus, the parameter vector is sparse, which is useful for features selection (ignore many irrelevant features).


## Worse case: L2 regularization causes #training examples needed to grow at least O(#irrelevant features)

L2 regularization encourages the sum of the squares  of parameters to be small.

Because in the worst case, number of samples needed grows linearly in the number of irrelevant features,
L2 is not good when only a few features are relevant and the training set size is small
relative to number of features.
