---
type: post
date: 2020-01-30
title: "Are arrays passed by pointer or reference in C++?"
---

Modified from [here](https://stackoverflow.com/questions/24057085/is-c-array-passed-by-reference-or-by-pointer)

Neither, actually, as an array cannot be passed either by pointer, reference, or value.

```c++
void foo(int[] arr);
```
is silently translated to
```c++
void foo(int* arr);
```

and
```c++
int[] array{1,2,3,4,5};
foo(array);
```
is silently translated to 
```c++
int[] array{1,2,3,4,5};
foo(&array[0]);
```
So really you're passing a pointer to the first array element.
