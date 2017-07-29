---
layout: post
title:  "Python inlining"
date:   2017-07-28 01:57:45 -0700
categories: python, coding style
---

Python inlining makes code more readable. 
Especially code read by many people for a complex application.

Therefore a function like

```python
def return_even_numbers_only(arr_of_nums):
	even_numbers = []
	for n in arr_of_nums:
		if n % 2 == 0:
			even_numbers += [n]
	return even_numbers
```

should be refactored to

```python
def return_even_numbers_only(arr_of_nums):
	return [n for n in arr_of_nums if n % 2 == 0]
```

Similarly, if-else statements should be inlined if possible.

```python
def is_even(n):
	if n % 2 == 0:
		return True
	else:
		return False
```

should be refactored to

```python
def is_even(n):
	return True if n % 2 == 0 else return False
```

Also, even for larger blocks of code, use fewer conditionals if possible.


```python
def get_fibonacci_number(n):
	if n == 0:
		return 1
	elif n == 1:
		return 1
	else:
		return get_fibonacci_number(n - 1) + get_fibonacci_number(n - 2)
```

could be rewritten as

```python
def get_fibonacci_number(n):
	if n == 0 or n == 1:
		return 1
	return get_fibonacci_number(n - 1) + get_fibonacci_number(n - 2)
```











