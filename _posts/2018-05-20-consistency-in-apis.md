---
type: post
title: "Consistency in APIs"
date: 2018-05-20
---

Summarized from [here](http://restlet.com/company/blog/2017/05/18/the-four-levels-of-consistency-in-api-design/).

## Why consistency matters

"Call a spade a spade".

Obeying the principle of least surprise.

With a REST API, a GET request should retrieve data, not delete it.
A 200 status should mean everything is OK.

Without consistent design, API users will be frustrated,
and either not use it or misuse it (and end up corrupting production data?)

## Global - being consistent with the world

REST APIs should respect the HTTP protocol,
follow practices like URI template,
and copy what well known API provides (e.g. Stripe/Google) do.

Being consistent in the data format use for timezone, currency, units
is also important, so users don't need to use the documentation.

## Local - being consistent within the API

If the same data is used in different resources, 
have the same name and type.
Use either camelCase or snake_case everywhere, but not both.

This lets users predict how an endpoint should work.

## Transversal - being consistent within your company/org

It's especially important so the company seems united
and not piecemeal, and in an era with micro-services that
interact with each other through APIs.

## Domain - conform to a standard 

For example, representing country codes using the ISO-3611 format
everywhere.
