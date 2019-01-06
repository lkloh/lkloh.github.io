---
type: post
title: "Mapping an observable"
date: 2019-01-04
---

Notes from this [tutorial](https://egghead.io/lessons/javascript-using-the-map-method-with-observable).

Obserables can be transformed by the `map` function.

For example, we can transform a click observable
listening to click events into a series of points
where the click happens:

```js
const button = document.getElementById(`button`);

// click observables
const clicks = Rx.Observable.fromEvent(button, `click`);

const subscription = clicks.forEach(
  function onNext(click) {
    alert(`I was clicked!`);
  }
);
```

into

```js
const button = document.getElementById(`button`);

// clicks transformed to points lazily
const points = Rx.Obserable.fromEvent(button, `click`)
  .map(e => ({x: e.clientX, y: e.clientY}));

const subscription = points.forEach(
  function onNext(point) {
    alert(`x coord: ${point.x}, y coord: ${point.y}`);
  }
);
```


