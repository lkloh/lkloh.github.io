---
type: post
title: "parentElement vs parentNode"
date: 2019-03-25
---

Summarized from [here](https://www.w3schools.com/jsref/prop_node_parentelement.asp).

They both return the parent element of a specified element.

They only differ when the parent is not an element,
as `parentElement` returns `null` while `parentNode` returns `document`.

To illustrate, given this HTML code:
```
<html>
  <head></head>
  <body>
    <div id="foo">
      <div id="bar"></div>
    </div>
  </body>
</html>
```
then

```js
const barEl = document.querySelector(`#bar`);
barEl.parentNode; // #foo node
barEl.parentElement; // #foo node

const docEl = document.documentElement;
docEl.parentNode; // document
docEl.parentElement; // null 
```

