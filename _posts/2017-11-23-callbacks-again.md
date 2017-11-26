---
layout: post
title:  "Callbacks again"
date:   2017-11-23
---

I encountered a problem somewhat like this,
except a lot more complicated with many more moving parts.
I was wondering why this script

```js
// GREATLY simplified version of the problem I got, it wasn't this obvious

function firstFunction() {
	setTimeout(function() {
		console.log('I always should come first!');
	}, 200);
}

function lastFunction() {
	console.log('I am always last to finish :(');
}

firstFunction();
lastFunction();
```

kept printing
```
I am always last to finish :(
I always should come first!
```

instead of
```
I always should come first!
I am always last to finish :(
```

It took me way longer than I should have to realize this was the issue,
as the real codebase obfusticated the problem with many other things.

The way to fix this is to alter `firstFunction`:
```js
// ES5 solution

function firstFunction(callback) {
	setTimeout(function() {
		console.log('I always should come first!');
		if (callback) {
			callback();
		}
	}, 200);
}

function lastFunction() {
	console.log('I am always last to finish :(');
}

firstFunction(lastFunction);
```


Problem was that I REALLY didn't want to mess with `firstFunction` if possible,
since in the actual problem it was very complicated and if possible,
I wanted to add a wrapper function instead.

Unfortunately, even ES6 required a modification to
`firstFunction` to print stuff in the right order.
Looks like there is no way around it.

```
// ES6 solution

function firstFunction() {
	return new Promise(function(resolve, reject) {
		setTimeout(function() {
			console.log('I always should come first!');
			resolve('Success');
		}, 200);
	});
}

function lastFunction() {
	console.log('I am always last to finish :(');
}

firstFunction().then(lastFunction);
```





