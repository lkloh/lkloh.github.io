---
layout: post
title:  "How many greenthreads should you allocate?"
date:   2017-10-02
---

Not too many! 

You should probably allocate more than you strictly needed,
since that gives some leeway for extra concurrent work to be done
by putting more threads to work.

In the example below, only 2 threads are technically needed,
by the example with 20 allowable threads runs consistently faster.

```py
import eventlet
eventlet.monkey_patch(os=True, select=True, socket=True, time=True)

import math
from timeit import default_timer as timer

def time_taken(func):
	def inner_func():
		start = timer()
		func()
		end = timer()
		print "%s time: %f \n\n" % (func.__name__, end - start)
	return inner_func

def sum_numbers():
	s = 0.0
	for i in range(100000):
		s += math.sqrt(i*i + 1.0)
	return s

@time_taken
def limited_threads():
	pile = eventlet.GreenPile(2)
	pile.spawn(sum_numbers)
	pile.spawn(sum_numbers)
	print [val for val in pile]

@time_taken
def many_threads():
	pile = eventlet.GreenPile(1000)
	pile.spawn(sum_numbers)
	pile.spawn(sum_numbers)
	print [val for val in pile]

if __name__ == '__main__':
	limited_threads()
	many_threads()
```






