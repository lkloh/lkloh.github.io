---
type: post
title: "Use CSS instead of JavaScript when possible"
date: 2018-01-25
---

Summarized from [here](https://hackernoon.com/in-simple-terms-css-vs-javascript-abc9d709399d).

## What hakes up the frontend

* HTML: What things are
* CSS: How they look
* JavaScript: What the other two can't (e.g. send requests to the backend)

## Rules on when to use what

* CSS > JavaScript
* HTML > JavaScript

Because CSS and HTML are declarative, so code is more concise,
while JavaScript is a more generic language that can do more things,
and thus can break your website in many more ways.

## Why use CSS/HTML over JavaScript

* A broken CSS rule is very unlikely to make your web-app crash, but a null value in JavaScript just might.
* Many ways that the browser/hardware can optimize CSS without the dev doing anything, as CSS is declarative.
* Users may use old browsers - CSS gives graceful degradation by default, not rendering any new styles, but when using JavaScript you have to make an explicit check for browser compatibility.
* Using a JavaScript animation library introduced extra dependencies and thus overhead for rendering/maintainence, while CSS/HTML does not incur dependencies as they are just generic web standards.

