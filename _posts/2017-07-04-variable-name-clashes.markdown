---
layout: post
title:  "Variable naming"
date:   2017-07-04
---

Different from the name of a library name/function.

```python
from datetime import datetime
from dateutil.relativedelta import relativedelta

def get_difference_in_seconds(start_time):
  time = datetime.now() - start_time
  return relativedelta(time).years
```

The variable `time` is also the name of a popular 
[library](https://docs.python.org/2/library/time.html).
Try not to do this, 
even if scoping ensures it won't cause problems.

Instead, this is a better name:
```python
from datetime import datetime
from dateutil.relativedelta import relativedelta

def get_difference_in_seconds(start_time):
  time_diff = datetime.now() - start_time
  return relativedelta(time_diff).years
```



