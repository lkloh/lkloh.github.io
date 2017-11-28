---
layout: post
title:  "ES6 analogies"
date:   2017-10-15
---

Summary of ES6 new features from 
[here](https://blog.pragmatists.com/top-10-es6-features-by-example-80ac878794bb).
Cut boilerplate!

# map

Applies a function to all elements in the input.

Python:
```py
colors = ['red', 'green', 'blue']

def capitalize_var(v):
	return v.upper();

capitalized_colors = list(map(capitalize_var, colors))
```

ES6
```js
let colors = ['red', 'green', 'blue'];

function capitalizedVar(v) {
	return v.toUpperCase();
}

capitalizedColors = arr.map(capitalizedVar);
```

# filter

Creates a list of elements for which a function returns true.

Python
```py
numbers = [i for i in range(5)]
even_nums = list(filter(lambda n : n % 2 == 0, numbers))
```

ES6
```js
numbers = [0, 1, 2, 3, 4]
let evenNums = numbers.filter(n => {return n % 2 === 0});
```

## Reduce

Python
```py
from functools import reduce

product = reduce((lambda n, m: n * m), range(1, 5))
```

ES6
```js
let arr = [1,2,3,4];
let produce = arr.reduce((acc, val) => acc * val, 1);
```



