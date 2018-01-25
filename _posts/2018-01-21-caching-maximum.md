---
type: post
title: "Length of time for caching"
date: 2018-01-21
---

Taken from [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Access-Control-Max-Age) - not even "summarized".

`Access-Control-Max-Age` is a HTTP header field that sets the maximum time a result
can be cached for. It is given in seconds.

You could write a large number of seconds like 9999999999,
but most major browsers restrict the maximum time results can be cached for to 
something sensible, such as 24 hours for Firefox and 10 minutes for Chrome.
So don't go crazy with trying to save on network latency.


