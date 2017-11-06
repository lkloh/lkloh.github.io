---
layout: post
title:  "Using webpack to render server-side JavaScript in the client"
date:   2017-11-01
---

![Node fails on client](https://{{ site.url }}/assets/2017/November/nov1_2017_require_failure){:class="img-responsive"}

Rendering server-side JavaScript on the browser would
[fail](https://github.com/lkloh/javascriptPlayground/tree/master/usingRequireInClient/no-rendered).

## Error

index.html
<html>
  	<head>
    	<title>Getting Started</title>
    	<script src='./index.js'></script>
    	<script>
    		var component = document.getElementsByClassName('component');
    		component.innerHTML = getComponentContent();
    	</script>
  	</head>

  	<body>
  		<div class='component'></div>
  	</body>
</html>


index.js
```
var _ = require('lodash');

function getComponentContent() {
  return _.join(['Hello', 'webpack'], ' ');
}

console.log(getComponentContent());
```

## Using Webpack

Follow instructions [here](https://webpack.js.org/guides/getting-started/).

Here's a [working version](https://github.com/lkloh/javascriptPlayground/tree/master/usingRequireInClient/webpack-demo).











