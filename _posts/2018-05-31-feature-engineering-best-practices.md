---
type: post
title: "Feature engineering practices"
date: 2018-05-31
---

Summarized from [here](https://elitedatascience.com/feature-engineering-best-practices).

## What feature engineering is

Creating new input features to improve performance of an ML model.

## Why bother

Improve predictive models.

## What it can help with

* Isolate key information
* Highlight patterns
* Bring in domain expertise

## How it fits in with an ML project

1. Data collection
2. Exploratory analysis
3. Data cleaning (remove duplications/ handle missing values/ fix mislabeled classes), etc
4. **Feature Engineering**
5. Model training
6. Prediction

## Indicator variables

Used to isolate key information,
by helping the ML algorithm focus on the important signal.

How to highligh key information
* Threshold: When studying alcohol preferences with a dataset comprised of  U.S. subjects,
  create an indicator for `age >= 21` to identify subjects that are legally
  allowed to drink.
* Combining multiple features: When predicting real estate prices,
  and if you have two features called `n_bathrooms` and `m_bedrooms`,
  and houses with 2 bedrooms and 2 bathrooms are very desirable,
  create an indicator variable `n_bathrooms == 2 && m_bedrooms == 2` to flag them.
* Special events: When modeling daily says for ecommerce, create an indicator variable
  for holidays associated with high shopping volume (e.g. Black Friday and Christmas).
* Groups of classes: When analyzing website conversions with a feature called `referral_origin`,
  flag those with the words `Facebook` or `Google`.

## Interaction Features

Highlight interactions between `>= 2` features.

But do not find all interactions between every pair of features,
or this cases "feature explosion" due to the power of combinatorics.

For example, given `house_built_date` and `house_purchase_date`,
you can produce `house_age_at_purchase` by finding their difference.

## Feature representation

Data does not always come in the ideal format, so you need to transform it to your ideal format.

For example, if you are analyzing ecommerce traffic and are given a feature called
`purchase_timestamp`, it may be more useful to extract the `purchase_hour`
and `purchase_day_of_week` to look for patterns in retail.
For example, more people shop on Friday than Monday,
and more people shop at 9pm than 9am.

## External data

Bringing in external data can boost performance.
For example, hedge funds compose financial datasets from multiple sources.

For example, given time series data with a `datetime` field,
you can use that `datetime` field to add in features from a different source.

Given a feature `zipcode`, you can add another feature such as `median_income_within_3_miles`.

## Post modeling error analysis

Use error analysis after exploratory analysis for feature engineering,
understand why the initial model performed poorly.

For example, look at predictions with a high error and understand the pattern
of test instances that caused poor predictions.
Use that pattern to form new features.

Or run an unsupervised clustering algorithm to help you spot patterns.

## Guidelines

* Engineer features that are intuitive to explain.
* Never touch the target variable, it gives very misleading results.

