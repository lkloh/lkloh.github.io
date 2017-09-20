---
layout: post
title:  "Variable naming"
date:   2017-07-04 01:57:45 -0700
---

Different from the name of a library name/function.

```python
from datetime import datetime
from dateutil.relativedelta import relativedelta

def get_difference_in_seconds(years_since_i_started_college):
  time = datetime.now() - time_i_started_school
  return relativedelta(time).years
```

The variable `time` is also the name of a popular 
[library](https://docs.python.org/2/library/time.html).
Try not to do this, 
even if scoping ensures it won't cause problems.



