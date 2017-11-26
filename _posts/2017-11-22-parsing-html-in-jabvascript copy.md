---
layout: post
title:  "Parsing HTML in JavaScript"
date:   2017-11-22
---

There are lots of ways to parse a HTML string into a DOM object.

Here's one that works:

```js
var domElem = $.parseHTML('<div>Hello World <a href="www.example.com">MyAwesomeExample!</a></div>');
```

will be parsed into
```
<div>
  Hello World
  <a href="www.example.com">
  	MyAwesomeExample!
  </a>
</div>
```

However, this does NOT work properly:
```
var domElem = $.parseHTML('<html><head>myHead</head><body>myBodyIsTheOnlyThingIWant</body></html>');
```

This will not return an object with a `head` and `body` as child nodes,
but just a jumble of text of this form:
`myHeadmyBodyIsTheOnlyThingIWant`.
Same thing happened for other methods of parsing HTML strings, such as `DOMParser` in 
JavaScript.
Could not retrive JUST the contents of `head` and `body` that I wanted.
Only tags like `div` or `a` could be retrieved.

If you want to peel off the `head` and `body` from a HTML string, you need to use regex.


