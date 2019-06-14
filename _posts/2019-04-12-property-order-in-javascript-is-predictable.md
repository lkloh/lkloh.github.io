---
type: post
title: "Property order in JavaScript is predictable"
date: 2019-04-12
---

Summarized from [here](https://www.stefanjudis.com/today-i-learned/property-order-is-predictable-in-javascript-objects-since-es2015/).

Since ES2015, the internal `ownPropertyKeys` method
uses specific rules to decide the order or properties.

But don't bank on this fact, as different browsers can order
them differently. So if you developed on Chrome and your user pulls
up your webapp in Safari your customer support team may get an
unpleasant surprise.




