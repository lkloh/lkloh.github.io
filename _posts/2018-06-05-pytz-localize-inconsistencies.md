---
type: post
title: "Pytz and timezones"
date: 2018-06-5
---

```py
import pytz
from datetime import datetime

tz = pytz.timezone('Europe/Berlin')
print repr(tz)
# <DstTzInfo 'Europe/Berlin' CET+1:00:00 STD>

d = datetime.now()
result = tz.localize(d)
print repr(result.tzinfo)
# <DstTzInfo 'Europe/Berlin' CEST+2:00:00 DST>

print repr(result.tzinfo) == repr(tz) 
# False
```

Inconsistencies are bad.
The abbreviation is actually [all that is different](https://stackoverflow.com/questions/24359540/why-doesnt-pytz-localize-produce-a-datetime-object-with-tzinfo-matching-the-t),
but you have to always use `localize` now, even if it means
converting a date into a timezone naive datetime to localize it back.

