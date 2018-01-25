---
type: post
title: "Timezone aware dates in Python"
date: 2018-01-25
---

This is a date i UTC time.

```py
from datetime import datetime

utc_datetime = datetime.utcnow()
```

And it does not have a timezone
```py
utc_datetime.tzinfo # None
```

To make it timezone-aware:
```py
from datetime import datetime
import pytz

utc_datetime = datetime.utcnow()
tz_singapore = pytz.timezone('Asia/Singapore') # UTC+08:00
singapore_datetime = tz_singapore.localize(utc_datetime)
print singapore_datetime # <DstTzInfo 'Asia/Singapore' SGT+8:00:00 STD>
```

