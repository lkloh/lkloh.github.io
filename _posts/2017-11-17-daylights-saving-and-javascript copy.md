---
layout: post
title:  "Daylights saving and JavaScript"
date:   2017-11-17
---

Motivated by [this article](https://swizec.com/blog/a-day-is-not-606024-seconds-long/swizec/6755).

A day is usually `24 * 60 * 60` seconds long, but not always due to daylights saving.

Look at this

```
// Generated in San Francisco, CA

var DAY_MILLISECONDS = 1000 * 60 * 60 * 24;
var WEEK_MILLISECONDS = DAY_MILLISECONDS * 7;


var regular_day = new Date('2017-11-01T02:00:00');
console.log('Not a daylights saving day: ' + regular_day);
console.log('Before daylights saving, day before: ' + new Date(regular_day.getTime() - DAY_MILLISECONDS));

console.log();

// Go back by 24 * 60 * 60 seconds
var after_daylights_saving_transition = new Date('2017-11-06T02:00:00');
console.log('After daylights saving: ' + after_daylights_saving_transition); // Sun Nov 05 2017 18:00:00 GMT-0800 (PST)
console.log('On aylights saving: ' + new Date(after_daylights_saving_transition.getTime() - DAY_MILLISECONDS)); // Sat Nov 04 2017 19:00:00 GMT-0700 (PDT)

console.log();

// Go back by a day using JavaScript's inbuilt function
console.log('After daylights saving: ' + after_daylights_saving_transition);
var day_before_daylights_saving = new Date(after_daylights_saving_transition); // Sun Nov 05 2017 18:00:00 GMT-0800 (PST)

day_before_daylights_saving.setDate(day_before_daylights_saving.getDate() - 1);
console.log('On daylights saving: ' + day_before_daylights_saving); // Sat Nov 04 2017 18:00:00 GMT-0700 (PDT)
```

Takeaways: Use inbuilt library functions/ an open source library with a good reputation
when dealing with time and timezones. 
Its really easy to mess it up yourself otherwise.


