---
layout: post
title:  "Eventlet hates Threading"
date:   2017-10-07
---

Python's threading library makes use of the system's native OS to schedule threads.
It make use of Python's global interpreter lock to make sure
shared data structures are accessed by only one thread at a time
to avoid race conditions.

Eventlet is made of greenthreads, which are different from normal threads.
The cooperatively yield to each other instead of being schedule by the OS.
This is to ensure shared data structures don't need locks.
This means a yield function must be explicitly called before another
green thread can access the shared data structure.
Since the OS doesn't need to schedule threads,
greenthreads are very cheap to deploy.

But you have to be careful when mixing greenthreads with system threads.
If a system thread is running, 
then it never calls the "yield" function. 
Then a greenthread may wait forever for a system thread to call "yield",
but the system thread will never do that,
because it expects the OS to schedule it for that.

It's lead to a large application written in Django that uses eventlet 
to deadlock and stall completely in the past.

```py
import eventlet
eventlet.monkey_patch(os=True, select=True, socket=True, time=True)

from eventlet.greenpool import GreenPool, GreenPile
import math
import time
import threading

def do_large_computation():
	s = 0
	for i in range(100000000):
		s += math.sqrt(i*i + 1)
	print s

def wait_forever():
	print 'wait_forever'
	while True:
		print 'hi'
		time.sleep(1)

def use_eventlet():
	pool = GreenPool(100)
	pile = GreenPile(pool)
	for i in range(10):
		pile.spawn(do_large_computation)
	print pile.next()

def use_threads():
	threads = []
	for i in range(10):
	    t = threading.Thread(target=wait_forever)
	    threads.append(t)
	    t.start()

if __name__ == '__main__':
	use_threads()
	use_eventlet()
```