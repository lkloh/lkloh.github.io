---
type: post
title: "Starting and stopping in different timezones"
date: 2018-02-14
---

When making a webapp that serves users in multiple timezones anywhere on Earth, it is important to remember:
* Users in UTC-12:00, the timezone furthest into the future, are the _last_ to **start** and also the __last__ to **finish**
* Users in UTC+14:00, the timezone furthest into the past, are the _first_ to **start** and the _first_ to **finish**

Suppose I am a marketing person for a grocery store with shops all over the world,
so I want to send a text message at 11am on Feb 17, 2018 (Saturday) to all my users to remind me to shop at my stores.
Clearly 11am in UTC-08:00 in San Francisco is not the same time as 11am in UTC+08:00 in Singapore.
The first user will get a message at 2018-02-16 T 21:00:00 UTC time (users in UTC+14:00 are the first to get the message)
and the last user will get the message at 2018-02-17 T 23:00:00 UTC time (users in UTC-12:00 at the last to get the message). 




