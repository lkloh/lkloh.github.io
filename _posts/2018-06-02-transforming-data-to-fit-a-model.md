---
type: post
title: "Transforming data to fit a model"
date: 2018-06-02
---

Summarized from [here](https://www.quora.com/In-laymans-language-Box-Cox-transformation-is-used-for-what).

Box and Cox wrote in ["An analysis of transformations"](https://www.nuffield.ox.ac.uk/users/cox/cox72.pdf)
that many data analysts often assume that data points are independently normally distributed
with constant variance. Their papre assumes that this model is appropriate
after some transformation has been applied to the data points so that it follows
and approximate Normal distribution.

## Why translate datasets into a Normally distributed dataset

There are many easy statistical techniques to work with Normally distributed data

## Example

Suppose you are modelling how well fiction books sold over the year.
Most books sell only a few copies, some books (like Harry Potter) sell
enormously well. So there is a long tail of books that sold a few copies,
and a small concentration sold very well.
Thus the average number of books sold could well be higher than the mode,
even though in a Normal distribution, mode, median, and mean are identical.

Thus, finding the "average number of books" sold is misleading,
as someone may think that they have a better chance of selling X number of books than they actually do.
As guessing the distribution is hard, and then figuring out the optimal analysis methods even harder,
it is easier to transform the data to make it more Normal.
The conventional statistical methods might work better.
For instance, it may be easier to take the square root or logarithm of the data points.

