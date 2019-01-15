---
type: post
title: "Perceived performance"
date: 2019-01-07
---

Summarized from [here](https://blog.teamtreehouse.com/perceived-performance).

There's been a lot written about how page load times can 
[significantly impact a business](https://developers.google.com/web/fundamentals/performance/why-performance-matters/). For example, BBC lost 10%
of users for every extra second it took for their page to load.
So investing in optimizing performance is important, but for a short term fix, there are also things you could do to impact how fast a user thinks your site is.

# Response times

The time taken for content to load.
0.1 seconds feels instantaneous, 1 second is ok but feels laggy,
and 10 seconds is the limit anyone will bother waiting for any
non-critical activity not related to their job/ credit card 
information being processed, etc.

## Improving the perceived response time

* Add a loading dialog to show the user
that something is happening after they clicked a button.
The loading progress bar is best if you can estimate
the time left to completion, but the spinning wheel is still
better than a static page.
* Use button states - make the button look different when you click
on it. The `:active` state is your friend.







