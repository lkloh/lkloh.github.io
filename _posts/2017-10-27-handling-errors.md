---
layout: post
title:  "Handling errors"
date:   2017-10-27
---

Recently I wrote a function that only a developer with 
access to the private repo would use.
No external customers would ever know that function exists.

```py

    
```



## External functions

Handling them carefully, with strong defenses.
Do your best effort.

## Internal functions

Anything goes wrong: fail fast and noisly right there.
Otherwise you risk someone screwing up part of your system without realising it.
This could be long and painful to recover from.