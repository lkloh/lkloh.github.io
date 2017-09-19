---
layout: post
title:  "Catching errors"
date:   2017-08-12 01:57:45 -0700
---

What's wrong with this?

```js
function getResponse(params) {
	return obtainNetworkResponse(params)
		.then(response => {
			console.log(response.result);
		})
		.catch(error => {
			this.notify(`something went wrong`);
			throw new Error(error);
		});
}
```

the `catch` method is called when the network request fails,
and an error gets throw.
That gets handled in the `catch` block.
So there's no need to throw an error again within that block.

```js
function getResponse(params) {
	return obtainNetworkResponse(params)
		.then(response => {
			console.log(response.result);
		})
		.catch(error => {
			this.notify(`something went wrong`);
		});
}
```
is sufficient.























