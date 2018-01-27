---
type: post
title: "Timezone offset in Python"
date: 2018-01-26
---

To get the timezone offset of any timezone in Python 2:

```py
import pytz

def get_timezone_offset_in_seconds(timezone_name):
  tz = pytz.timezone(timezone_name)
  now = datetime.utcnow()
  offset = tz.utcoffset(now)
  return offset.total_seconds()
```

Then we have
```py
get_timezone_offset_in_seconds('Asia/Singapore') # 28800.0
get_timezone_offset_in_seconds('US/Hawaii') # -36000.0
```




