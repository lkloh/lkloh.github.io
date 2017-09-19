---
layout: post
title:  "Stopping Time"
date:   2017-08-05 01:57:45 -0700
---

Sort of. 

If there's a time-dependent Python function you want to test, you don't really want to write

```
from datetime import datetime, timedelta
import time

def test_request(self):
	time_before = datetime.now()
	time.sleep(5)
	time_request_finished = make_request(self.params)
	assert (time_after - time_before).total_seconds() <= 5
```

Then you'll have to wait a long time for the test to finish running.

Instead, with the [freezegun](https://github.com/spulec/freezegun) library,
you could instead run the test immediately by writing

```
from datetime import datetime, timedelta
import time

def test_delivered_cookies_within_20_min(self):
	time_before = datetime.now()
	advanced_time = time_before + timedelta(seconds=5)
	with freeze_time(initial_datetime) as frozen_datetime:
		frozen_datetime.move_to(advanced_time)
		time_request_finished = make_request(self.params)
		assert (time_request_finished - time_before).total_seconds() <= 5
```

Now your test doesn't actually need to take 5 seconds (or more) to run.

































