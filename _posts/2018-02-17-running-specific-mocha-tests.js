---
type: post
title: "Running specific mocha tests"
date: 2018-02-17
---

Summarized from [here](https://jaketrent.com/post/run-single-mocha-test/).

## Run a single test suite

Given

```js
describe(function() {
  // tests
});
```
change it to

```js
describe.only(function() {
 // tests
});
```

## Run one test

```js
it(function() {
  // test
});
```

and change it to

```js
it.only(function() {
  // test
});
```

## Skip a test

Both of these will run

```js
it(function() {
  // test 1
});

it(function() {
  // test 2
});
```

but to run only test 1, change it to

```js
it(function() {
  // test 1
});

it.skip(function() {
  // test 2
});
```

