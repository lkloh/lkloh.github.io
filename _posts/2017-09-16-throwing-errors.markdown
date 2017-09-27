---
layout: post
title:  "Which network error should a server throw?"
date:   2017-09-16
---

If the client send the server a problematic request, 
throw them a 4xx error
to tell them to fix it on their side.

The client sent a valid request,
but the server has some issues and can't serve the client,
throw a 5xx error to tell the client to retry later.

Also explain what went wrong to the client.
Read more [here](http://restcookbook.com/HTTP%20Methods/400-vs-500/).