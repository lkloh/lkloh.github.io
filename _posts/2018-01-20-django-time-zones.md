---
post: type
title: "Store time in UTC in your database"
date: 2018-01-20
---

Summarized from [here](https://docs.djangoproject.com/en/2.0/topics/i18n/timezones/).

Even if you're using Django, which does several nice things when you
enable timezone support:
* Stores datetime information in UTC in the database, even if the information
  originated from a different timezone
* Translate the datetime from UTC to the end user's timezone

So, minimal confusion about the exact time an event was supposed to occur at.
If a site has users in multiple timezones, the owner
can still display datetime information according to the users' time
to minimize confusion.

## Best practices for storing time

* Store it as UTC in the database - even if your users are in the same timezone.
  Some countries have Daylight Saving Time, so if you stored your time as 
  "10 hours from 19:00 pm on March 10, 2018", 
  then instead of an event occuring at 05:00 am on March 11, 2018,
  it would occur at 06:00 am on March 11, 2018 due to the time transition.
* Its very hard to change the way you stored data once you start scaling
  to other timezones.
