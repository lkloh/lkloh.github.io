---
layout: post
title:  "At most 3 levels of indents"
date:   2017-11-27
---

I was writing something with 4 levels of indents. Bad.

```py
if is_human(living_being): # 1st indent
	if living_being.get('gender'): # 2nd indent
		cut_hair_off(living_being)
		if living_being.get('emotion') == 'negative': # 3rd indent
			if living_being.get('heart_rate') > 100:  # 4th indent
				kill_it(living_being)
			else:
				sell_it(living_being)
		else:
			kill_it(living_being)
	else:
		raise "No gender provided"
```

3 levels of indents should be the maximum. The way to fix the above is to do:
```py
if !is_human(living_being):
	return
if living_being.get('gender'): # 1st indent
	cut_hair_off(living_being)
	if living_being.get('emotion') == 'negative': # 2nd indent
		if living_being.get('heart_rate') > 100: # 3rd indent
			kill_it(living_being)
		else:
			sell_it(living_being)
	else:
		kill_it(living_being)
else:
	raise "No gender provided"
```

