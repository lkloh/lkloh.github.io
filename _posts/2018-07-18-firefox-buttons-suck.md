---
type: post
title: "Firefox buttons don't work properly"
date: 2018-07-18
---

Up until sometime this week, Firefox buttons don't work as expected.

For example,
```js
$(`button`).click(e => {
  console.log(`You clicked me!`);
});
```
worked as expected in Chrome and Safari, but it didn't work in Firefox.

The [workaround](https://stackoverflow.com/questions/16280684/nesting-a-inside-button-doesnt-work-in-firefox)
is to not use buttons at all, but instead style a div as a button.

```js
$(`div.button`).click(e => {
  console.log(`You clicked me!`);
});
```
