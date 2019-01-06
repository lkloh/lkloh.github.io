---
type: post
title: "The observable"
date: 2018-01-03
---

The [Observable](https://egghead.io/lessons/rxjs-introducing-the-observable)
is a collection that arrives over time.
It can be used to model events.
For example, this [tutorial](https://egghead.io/lessons/rxjs-introducing-the-observable) describes how to use an observable to trigger
an action after one button click, then disable
the trigger after the first time the button is clicked.
You can try out the code on [jsbin.com](http://jsbin.com/).

Normally, to make a button do something, you would write
```js
const button = document.getElementById('button');

const handler = e => {
  alert(`I was clicked`);
  removeEventListener();
  removeListener(`click`, handler);
}

removeListener = () => {
  button.removeEventListener(`click`, handler);
};

button.addEventListener(`click`, handler);
```

But if you use an observable to register click events to
the button, you would do:

```js
const Observable = Rx.Observable;

const subscription = {
  Observable.fromEvent(button, `click`).forEach(
    function onNext(e) {
      alert(`clicked`);
      subscription.dispose();
    },
    function onError(err) {
      console.log(err);
    },
    function onCompleted() {
      console.log(`done`);
    }
  );
}
```



