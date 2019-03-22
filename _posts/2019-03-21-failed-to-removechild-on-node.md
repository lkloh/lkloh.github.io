---
type: post
title: "Failed to execute removeChild on Node"
date: 2019-03-21
---

This bit of code will throw a `Failed to execute removeChild on Node` error.
```js
var wrapper = document.createElement("div");
wrapper.innerHTML = '<div id="hello">Hello World!</div>';
document.body.appendChild(wrapper);
setTimeout(function() {
  var helloNode = document.querySelector(`#id`);
  document.body.removeChild(`helloNode`);
}, 1000);
```

Reason is that the node with id `hello` is not a direct child of `document.body`.

To avoid such confusion and digging around, a good way to remove a node is:
```js
var helloNode = document.querySelector(`#id`);
if (helloNode && helloNode.parent) {
  helloNode.parent.removeChild(helloNode);
}
```

Thanks [StackOverflow](https://stackoverflow.com/questions/42956884/failed-to-execute-removechild-on-node)!

