---
type: post
title: "Dirichlet distribution"
date: 2018-05-29
---

[Summarized from here](https://www.quora.com/What-is-an-intuitive-explanation-of-the-Dirichlet-distribution).


## What is the Dirichlet districution?

* Distribution of distributions
* Sampling over a probability simplex (a bunch of numbers that sum to 1),
  such as (0.1, 0.9), (0.05, 0.15, 0.20, 0.30).
  These numbers represent probabilities over K distinct categories.


## What the Dirichlet distribution can be used to represent

K-dimensional Dirichlet distribution has K parameters (any positive number).
Example: (23, 6, 32, 39).


## The normalization constanst

To normalize these parameters to form a probability distribution, 
divide them by their sum (100 in this case) write
100 * (0.23, 0.06, 0.32, 0.39).
The probabilities (23%, 6%, 32%, 39%) are the mean value of the Dirichlet.

### High normalization constant

The higher the normalization constanct (sum of the K parameters),
the closes the samples to the mean.
Since 100 is quite high, most samples are close to (23%, 6%, 32%, 39%).

### Low normalization constant

When it is close to 0, variance gets higher.
For example (0, 0, 1, 0),
getting far from the mean.


## Latent Dirichlet Allocation (LDA)

Used in classifying documents by subject.
Represents documents as a mixture of topics that have the own
probability distribution of possible words.

Documents are distributions of topics that are distributions of words.







