---
layout: post
title:  "Generators help you save memory"
date:   2017-10-21
---

Generators in function help generate values on demand,
instead of generating values all at one go and storing them in RAM.
They are especially helpful when generating large amounts of data that will
not fit into memory.
Or just saving memory in general, even if it fits.

In the example below, you save a TON of memory by generating values on the fly.
As in, something like 38 MB without a generator vs 5 Mb with one.

```py
# Inspired by https://wiki.python.org/moin/Generators
import resource

def output_peak_memory_usage_of_function(func):
	def wrapper(*args, **kwargs):
		func(*args, **kwargs)
		mega_bytes_used = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000000.0
		print 'Peak memory usage for function %s: %f Mb' % (func.__name__, mega_bytes_used)
	return wrapper

@output_peak_memory_usage_of_function
def calculate_sum_by_creating_list_in_memory(n):
	i = 0
	arr = []
	while i < n:
		arr += [i]
		i += 1
	return sum(arr)

@output_peak_memory_usage_of_function
def calculate_sum_by_creating_list_with_generator(n):	
	def list_generator(n):
		i = 0
		while i < n:
			yield i
			i += 1
	return sum(list_generator(n))

if __name__=='__main__':
	calculate_sum_by_creating_list_with_generator(1000000)
	calculate_sum_by_creating_list_in_memory(1000000)
```

And when using Python's inbuilt functions,
using `xrange` instead of `range` in  Python 2,
as `xrange` uses a generator while `range` creates the objects
in memory.
Memory savings aren't as significant though,
and in Python 3 `xrange` and `range` will both use generators.


```py
import resource

def output_peak_memory_usage_of_function(func):
	def wrapper(*args, **kwargs):
		func(*args, **kwargs)
		mega_bytes_used = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1000000.0
		print 'Peak memory usage for function %s: %f Mb' % (func.__name__, mega_bytes_used)
	return wrapper

@output_peak_memory_usage_of_function
def python_xrange():
	lst = [i for i in range(1000000)]

@output_peak_memory_usage_of_function
def python_range():
	lst = [i for i in xrange(100000)]

if __name__=='__main__':
	calculate_sum_by_creating_list_with_generator(1000000)
	calculate_sum_by_creating_list_in_memory(1000000)
	python_range()
	python_xrange()
```

