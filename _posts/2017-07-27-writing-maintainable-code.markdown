---
layout: post
title:  "Writing maintainable code"
date:   2017-07-27
---

Best takeaways from the [community here](https://stackoverflow.com/questions/162805/writing-maintainable-code):


* Write 5 lines of simple code that is easy to understand, 
	not esoteric code in one line that very few people know.
	Write code the way you would speak to a human being.
* Keep classes and methods small
* Refactor your code every so often
* DRY - Don't repeat yourself
* Reach the library documentation carefully to see if you really need any type of function
	before writing your own
* Max #indents in a function should be 3 at worst.
	```py
	# too many indents
	if is_human(living_being):
		if living_being.get('gender')xs:
			cut_hair_off(living_being)
			if living_being.get('emotion') == 'negative':
				if living_being.get('heart_rate') > 100:
					kill_it(living_being)
				else:
					sell_it(living_being)
			else:
				kill_it(living_being)
		else:
			raise "No gender provided"
	else:
		kill_it(living_being)
	```
* Be consistent with styles
* Have a dedicated method for each different task 
* Automated unit tests - changing code is less risky
* Design before writing code. Talk to someone else first.
* Use linters
* Name things properly. Long names are fine. No abbreviations allowed.









