---
type: post
title: "Handling outliers with data processing: Capping at threshold
date: 2018-06-03
---

## What it means

Winsorize the data: Replace outliers with a more normal value.

## Finding the Winsorized mean

The Winsorized mean is found to 
make the sample mean more descriptive of a typical data point,
as means are easily skewed by outliers.

To get a Winsorized mean, sort the data and replace the
k smallest values by the (k+1)st smallest value;
and replace the k largest values by the (k+1)st largest value.
Mean of the new set of numbers is the Winsorized mean.

```
k = 4

0 0 1 1 2 3 4 4 4 4 4 4 5 5 5 5 5 6 6 7
X X X X                         X X X X

becomes

2 2 2 2 2 3 4 4 4 4 4 4 5 5 5 5 5 5 5 5

windorized mean: 3.85
```

## Use cases

* Symmetric datasets only!
* Datasets that are so large that it does not make sense for a human to inspect outliers.


## Things to look out for

Throwing away data that seems "wrong" is data modification and generally a bad practice.
Modifying data invalidates statistical analysis.
It's usually appropriate only if the outliers are there for a reason (e.g. 
you know your data collection equipment malfunctioned and collected weird values
as some point in time).

Otherwise, outliers should not be removed as they contain valuable information as well
(e.g. flag credit card fraud).




