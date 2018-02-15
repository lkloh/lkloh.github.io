---
type: post
title: "Anywhere on earth"
date: 2018-02-13
---

Dealing with users in multiple possible timezones is a pain.
Here's some code to check whether the start time is before the stop time for an event,
and the kicker is that the timezones of the start time and stop time could potentially be different.

```js
function start_before_stop(start_str, stop_str, timezone) {
  if (timezone) {
    // start time and stop time in same timezone
    var start_timestamp = moment.utc(start_str).valueOf();
    var stop_timestamp = moment.utc(stop_str).valueOf();
    return start_timestamp < stop_timestamp;
  } else {
    // start time and stop time could be in any timezone on earth
    // start time could be in UTC-12:00, happening 12 hours in the future
    // stop time could be in UTC+14:00, happened 14 hours ago
    return moment.utc(start_str).valueOf() + 12 * 3600 * 1000 < moment.utc(stop_str).valueOf() - 14 * 3600 * 100;
  }
}
```


