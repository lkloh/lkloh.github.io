---
layout: post
title:  "Errors are exceptional"
date:   2017-08-10 01:57:45 -0700
---

All other "things going wrong" should be _expected_.

More is outlined [here](https://martinfowler.com/articles/replaceThrowWithNotification.html),
but the summary is:

When doing something like
```python
def validate_phone_number(phone):
	if re.compile(r'^(\d{3})-(\d{3})-(\d{4})$').match(phone):
		return True
	else:
		raise Exception('Wrongly formatted phone number')
```

We don't want to throw an exception here,
because when taking in user input, 
it should be expected to some users will provide invalid input.

Thus something like
```python
def validate_phone_number(phone):
	if re.compile(r'^(\d{3})-(\d{3})-(\d{4})$').match(phone):
		return True
	else:
		notify_error(`Invalid phone number`)
```
would be what you want to do.

You should only raise an exception when something happens that is truly unexpected,
such as when `/usr/bin` is not present,
since it is expected that a unix system should have that directory.
























