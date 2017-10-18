---
layout: post
title:  "Flattening a list of lists in Python"
date:   2017-10-17
---

# Yes

```py
arr = [[1,2], [3], [4,5]]
flattened_arr = [e for lst in arr for e in lst]
```


Which is equivalent to
```py
arr = [[1,2], [3], [4,5]]

flattened_arr = []
for lst in arr:
	for e in lst:
		flattened_arr += [e]
```
which operates in linear time.

# No

```py
arr = [[1,2], [3], [4,5]]
flattened_arr = sum(arr, [])
```

which is equivalent to

```py
from functools import reduce
import operator

arr = [[1,2], [3], [4,5]]
flattened_arr = reduce(operator.add, arr, [])
```

which essentially does this:
```
sum([[1,2], [3], [4,5]], [])
	= sum([[3], [4,5]], [1, 2])
	= sum([[4,5]], [1, 2, 3])
	= [1, 2, 3, 4, 5]
```
which makes lots of copies of of sublists to flatten the array.

Thanks to [this post](https://mathieularose.com/how-not-to-flatten-a-list-of-lists-in-python/) 
for educating the public.



