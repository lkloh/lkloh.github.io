---
layout: post
title:  "Patching random"
date:   2017-10-04
---

You can patch the random library to make it always return the same value like this.
There are two obvious ways to do it:


```py
import random
from unittest.mock import patch

@patch.object(random, 'random')
def get_random_float_patch_object(mock_random):
	mock_random.return_value = 0.7
	print(random.random())

@patch('random.random')
def get_random_float_patch(mock_random):
	mock_random.return_value = 0.5
	print(random.random())

if __name__ == '__main__':
	get_random_float_patch()
	get_random_float_patch_object()
```


Read more [here](https://stackoverflow.com/questions/18191275/using-pythons-mock-patch-object-to-change-the-return-value-of-a-method-called-w).


If you're patching more than one function, you have to do it in reverse order:
```py
import math
import random
from unittest.mock import patch

@patch.object(math, 'cos')
@patch.object(random, 'random')
def patch_order(mock_random, mock_math):
	mock_random.return_value = 0.7
	mock_math.return_value = 4.0 # -1 <= cos(x) <= 1 in practice
	print(random.random())
	print(math.cos(0))

if __name__ == '__main__':
	patch_order()
```







