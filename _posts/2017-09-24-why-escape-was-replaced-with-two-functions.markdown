---
layout: post
title:  "Why escape was deprecated in JavaScript."
date:   2017-09-24 11:46:37 -0700
---

According to its [documentation](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/escape),
the `escape` function takes in a string and returns a new string in which 
certain characters are replaced with a hexadecimal sequence.
For example,
```js
escape("abc123") = "abc123";
escape("?%") = %3F%25;
``` 


`escape` has since been deprecated and replaced with two functions,
`encodeURI` and `encodeURIComponent`.
This is because `escape` was mainly for encoding url parameters,
perhaps when making a GET request for instance.
Now why are two functions needed to replace it? Take a look at these results:

```js
encodeURI("abc123") = "abc123";
encodeURI("?%") = "?%25";
```

and


```js
encodeURI("abc123") = "abc123";
encodeURI("?%") = "%3F%25";
```

Essentially, `encodeURIComponent` does the same thing as `escape`. 
So why does `encodeURI` exist as well?

Take a look at what happens when encoding a URL with these:

```js
escape("") 
	= "https%3A//www.collegefashion.net/search%3Fquery%3Dblazers"
encodeURI("https://www.collegefashion.net/search?query=blazers") 
	= https://www.collegefashion.net/search?query=blazers
encodeURIComponent("https://www.collegefashion.net/search?query=blazers") 
	= https%3A%2F%2Fwww.collegefashion.net%2Fsearch%3Fquery%3Dblazers
```

It's so that you can now pass in the entire URL with parameters to `encodeURI`
to return the properly formatted URL,
instead of formatting the parameters with 
just `encodeURIComponent` or `escape`
and having to think about how to format it properly.
```js
encodeURI("https://www.collegefashion.net/search?query=blazers") 
	= https://www.collegefashion.net/search?query=blazers
```









