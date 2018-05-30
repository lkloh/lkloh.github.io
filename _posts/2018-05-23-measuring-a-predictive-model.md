---
type: post
title: "Measuring a predictive model"
date: 2018-05-23
---

Example from [here](http://www.theanalysisfactor.com/sensitivity-and-specificity/)
- its really well written!

## Example use case of a predictive model

Predicting whether the true owner of a credit card is performing a
financial transaction (e.g. buying groceries at a store), 
or the transaction is fraudulent, 
performed by a thief who stole the owner's card.

## Measuring the accuracy of model predictions on binary outcomes

* **Accuracy** - percentage of time the model makes a correct prediction
* **Sensitivity** - `truePositive / (truePositive + falseNegative)`.
  Of all the transcations that were truly fraudulent,
  how many did the model correctly predict as fraudulent?
* **Specificity** - `trueNegative / (trueNegative + falsePositive)`.
  Of all the transactions that were done with the owner's consent,
  how many did the model predict were legitimate?

Ideally, sensitivity and specificity are both high,
but there is usually a tradeoff - raising one would lower the other.
One must pick a threshold for the probability of fraud before flagging it as fraud.
Too sensitive and you piss off angry credit card users who got blocked on vacation;
not sensitive and you piss of angry credit card users who were defrauded of money.



