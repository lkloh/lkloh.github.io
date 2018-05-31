---
type: post
title: "Class imbalance"
date: 2018-05-28
---

[Summarized from here](https://elitedatascience.com/imbalanced-classes).


## When a dataset has "class imbalance"

The dataset has a disproportionate ratio of observations in each class,
a common problem in real world datasets.
Imbalanced classes can cause issues with accuracy,
making training a model harder.


## Some reasons why class imbalanced datasets occur

You're trying to train a model to detect a rare diseases on dataset
of patient samples. But if the disease is rare (e.g. occurs in 2% of the population),
if you used this as your model:

```py
def has_disease(patient):
  return False
```

it would have a 98% accuracy.
That accuracy is a problem as for patients with the disease, you have 0% accuracy.
The overall accuracy is high only because most patients do not have the disease,
not due to the model being predictive.

Since many ML algorithms optimize for overall accuracy, class imbalanced datasets become a problem.


## Ways to improve a model trained on an imbalanced class dataset

### Downsampling

Randomly remove observations from the majority class(es)
to avoid them from dominating the algorithm.
Resampling without replacement is a common way to do this.

### Changing the performance metric

AUROC (Area under the curve), which represents the likelihood of the model
distinguishing observations from two classes.
So this measures P(model ranks an instance into the correct class).

### Penalized learning algorithm

Increases the cost of classification mistakes on the minority class.
Penalize mistakes on the minority class proportional to how under represented it is.

### Decision tree

Hierarchical structure lets decision trees learn signals from both classes.

### Data augmentation

Resample from minority classes and slightly perturb their values,
so the dataset becomes class-balanced

### Combine minority classes

Combine minority classes of the target variable for multi-class datasets.

Example: Given a dataset on young college students
from a university (who are usually healthy),
predict whether a student is healthy or diseased.
Combine several classes of biological markers for different dieases
(e.g. cancer, HIV) together as you care about predicting whether a student is healthy,
not the type of disease they have.

## Use Anomaly detection

Majority profile: majority class

Underrepresented profile: Reframe it as an outlier/ rare event 

























