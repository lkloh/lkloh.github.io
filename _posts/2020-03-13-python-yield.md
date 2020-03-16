---
type: post
date: 2020-03-13
title: "Python YIELD"
---

Summarized from [here](https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do).

The `yield` keyword in Python is used to create a generator.

```python
def make_generator():
    for i in range(10):
        yield i
```

The key thing about generators is that they generate values on demand, instead of storing all the values in memory at once. Useful to lower memory usage.
```python
gen = make_generator()

for i in gen:
    print(i)
```