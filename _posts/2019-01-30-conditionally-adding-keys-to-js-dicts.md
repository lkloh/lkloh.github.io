---
type: post
title: "Conditionally adding keys to JavaScript Objects"
date: 2019-01-30
---

Summarized from [here](https://stackoverflow.com/questions/11704267/in-javascript-how-to-conditionally-add-a-member-to-an-object)
and [here](https://medium.com/@mikeh91/conditionally-adding-keys-to-javascript-objects-using-spread-operators-and-short-circuit-evaluation-acf157488ede).

I wanted to accomplish this.
```js
function processDict(d) {
  const processed = {
    sweets: d.fruits,
    greens: d.vegetables,
  };
  if (d.hasOwnProperty(`moneyInUSD`)) {
    processed.moneyInEuros = usdToEuro(d.moneyInUSD); 
  }
  return processed;
}
```

but that is quite verbose.

A way to shortcut this is
```js
function processDict(d) {
  return {
    sweets: d.fruits,
    greens: d.vegetables,
    ...(!!d.moneyInUSD && (moneyInEuros: usdToEuro(d.moneyInUSD)),
  };
}
```

Basically you can add a conditional key to an object by doing
```js
const d = {
  ...(condition && {myKey}),
}
```
and `myKey` is only added to the object if `condition` evaluates to true.
This works because in JavaScript, the `&&` and `||` operators
return the value of the last expression that is evaluated in the statement.

## Edit

Turns out a clearer way to do this is
```js
function processDict(d) {
  return {
    sweets: d.fruits,
    greens: d.vegetables,
    ...(d.moneyInUSD ? {moneyInEuros: usdToEuro(d.moneyInUSD)} : {}),
  };
}
```




