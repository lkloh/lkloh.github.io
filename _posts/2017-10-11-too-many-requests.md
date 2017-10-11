---
layout: post
title:  "429: Too many requests"
date:   2017-10-11
---

If a user sends too many requests to a site and you need to rate limit them:
return a 429 error that also explains the maximum number of requests 
they may make in any given time period.

No caching the response obviously!
Or the user won't get the desired 200 response
once enough time has passed that he can
now access the site again.























