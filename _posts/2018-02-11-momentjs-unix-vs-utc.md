---
type: post
title: "Difference between Unix and UTC time"
date: 2018-02-11
---

According to [Reddit](https://www.reddit.com/r/explainlikeimfive/comments/325ein/eli5what_is_the_difference_in_unix_utc_and/),
* Unix time: Number of seconds since 1970-01-01 T 00:00:00 UTC. 
  Often used to track time on Linux.
* UTC time: A wasy to measure time without taking time zones into account.
  Based on the amount of time it takes the prime meridian at Greenwich, London to line up with the Sun.

This means that UTC time and Unix is different, as one is based on time that elapsed since a certain marker in history,
the other can vary depending on orbital mechanics of the Earth.

Typically when dealing with time, UTC time is preferred instead of Unix time.

I tried to use the MomentJS library to get time now.
I used `var now = moment().unix()` to get the timestamp in seconds but someone told me that
`var now = moment.utc().valueOf()` to get the timestamp in milliseconds was preferable.




