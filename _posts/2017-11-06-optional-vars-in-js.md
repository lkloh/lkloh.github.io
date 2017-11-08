---
layout: post
title:  "Optional function parameters in JavaScript"
date:   2017-11-06
---

According to [StackOverflow](https://stackoverflow.com/questions/12797118/how-can-i-declare-optional-function-parameters-in-javascript):

## ES5

```
function func(mandatory, optional) {
	optional = optional || "default";
	// optional is set to optional or "default"
	...
}
```


## ES6

```
function func(mandatory, optional = "default") {
	...
}
```



