---
type: post
title: "Parametric vs non-parametric models"
date: 2018-05-12
---

Summary from [here](https://www.quora.com/What-is-the-difference-between-a-parametric-model-and-a-non-parametric-model).

## Parametric model

Stateless.

To predict value, you need to know just the parameters for the model.

For example, given a linear model 
for the price of a house over time, where `t` is time and `p` is the housing price:
```
p = mt + c
```

To predict the price of the house at any time `t` (perhaps `t` is the year 2019),
it is enough to know the parameters `m` and `c`, more.
You do not need to know what the values of `p` were for `t = 2016, 2017, ...`, etc).

## Non-parametric model

Stateful.

Uses information about the current state to help predict future data.

Parameters are said to be infinite in dimensions and thus captures the data more accurately
than stateless parametric models.

More accurate predictions, but not always used as it is harder to explain
the factors that make up a predicted value,
and being able to explain how your model came up with a prediction is important for trust.

