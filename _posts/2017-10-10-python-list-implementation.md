---
layout: post
title:  "Python list implementation"
date:   2017-10-10
---

Python lists are variable-length arrays, according to the 
[docs](https://docs.python.org/2/faq/design.html#how-are-lists-implemented).

The implementation uses a contiguous array of references to other objects,
and keeps a pointer to that array and the array's length in a list head structure.

```
 ----
|    | ---> size 4
 ---- 
  |
  | arr           ----
  |            > |    |
  V           /   ----
 ----        /--
|    | ----> |  |
 ----      /  --        ---
|    |---------------> |   |
 ----    /              ---
|    | \/
 ----  /\ 
|    |/  \
 ----     \
           \
            >
          -----
         |     |
          ----- 
```

Thus indexing `a[i]` takes constant time.

When items are appended, the array of references is resize by some multiple
of the original size, 
so that the next few times something is inserted does not use an actual resize.



































