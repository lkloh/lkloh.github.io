---
type: post
title: "Train and test on separate datasets"
date: 2018-04-29
---

Training and testing on the same dataset causes potential overfitting to the data.
Your model may perform well on the test dataset as it was trained on it,
but terribly on a different dataset.

What you should do is to train on a training dataset,
verify on a test dataset that is distinct from the training dataset.

Summary of [this Quora post](https://www.quora.com/Why-do-we-have-separation-of-data-into-training-held-out-and-test-data) on how to train and test data.

## Training and testing on the same dataset

Pros:
* Datasets can be hard/expensive to come by.
  In this way you get the maximum amount of data to train on.

Cons
* Overfitting the model to that particular dataset you trained things on.
  If the dataset has mistakes (due to typos by whoever created it, etc),
 those mistakes may present in the model as well.
* The overfitted model works well on the dataset trained on, badly on other datasets.
  So its not useful for making predictions and all the other stuff you
  made the model for in the first place.

## Cut the dataset in half: Train on one half, test on the other half

Pros
* Avoid overfitting to the training dataset.

Cons
* Need to figure out which part of the dataset is "better" for training,
  which is "better" for testing.
* Less data to train on

## Cut the dataset in N pieces for some N > 5. Train on each different piece and test on the others. Average the parameters for each partitioned dataset.

Also known as N fold cross validation.

Pros
* Use all the data to train the model.

Cons
* The model was tested on data that had been used for training.
  May not work on completely unseen data.

## Cut the dataset into N+1 pieces for N > 5. Keep the last bit for testing. Use the remaining N partitions to train and develop a model and average the parameters.

Pros
* Use most of the data to train the model
* Testing on completely unseen data

Cons
* You do lose a bit of data for training (problematic if your dataset was small to start with)
* More complicated logistics



