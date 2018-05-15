---
type: post
title: "Choosing a classifier"
date: 2018-05-14
---

Summarized from [here](https://nlp.stanford.edu/IR-book/html/htmledition/choosing-what-kind-of-classifier-to-use-1.html).

# Questions to ask

## How much training data is available?

The major challenge for training a ML classifier in a real application.
Usually O(n^3) examples from each class are need to produce a good classifier.

## When must the classifier be deployed?

* ASAP: Pick carefully!
* Take your time: spend it getting and cleaning data

## What if the training data is not labeled?

Write your own rules to label them

```
if (wheat or grain) and not (whole or bread) then c = grain
```

It takes a lot of time to make a good rule and maintain it though.


# If you have little labeled data

Accept that your classifier is not going to be great.

## If you want to train a supervised classifier

Use a classifier with high bias (e.g. Naive Bayes) that is relatively simple.

## Get more labeled data ASAP

* Best case: get humans to label data
* Not so ideal: Active learning - algorithm decides which documents a human should label - reduces costs of labeling


# If there is a reasonable amount of labeled data

Use an SVM


## If there is a lot of labeled data

Most classifiers would work well.

Choose the classifier that scales best or runs most efficiently.

