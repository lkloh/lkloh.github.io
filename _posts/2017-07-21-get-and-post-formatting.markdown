---
layout: post
title:  "Get and Post formatting in Javascript"
date:   2017-07-21
---

## Get

Used for viewing data, all required data passed in the URL. Meaning that when sending parameters over, the URL in the request should look something like `http://example.com?name=jane&age=21`

## Post

Used for altering data.
Additional data is sent in the body of the http request.
Since you should use JSON (language agnostic format) to send stuff over the network,
	and if your body is a Javascript object like
	```js
	const params = {
		name = `Jane`,
		age = 21,
	};
	```
	you'll need to call `JSON.stringify(params)` to
	pass this over in the body of the post request.


