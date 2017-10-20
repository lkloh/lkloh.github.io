---
layout: post
title:  "Circular Dependency Imports"
date:   2017-10-19
---

Running `python alice.py`

```
alice.py
 -----------------------------------
| from bob import bobby             |
|                                   |
| def wonderland():                 |
|	return bobby() + ' loves Alice' |
|                                   |
| if __name__ == '__main__':        |
| 	print wonderland()              |
 -----------------------------------


bobby.py
 ------------------------------
| from alice import wonderland |
|                              |
| def bobby():                 |
|   return 'Bob'               |
  ------------------------------
```

Will throw an error as both files depend on each other.

To fix this, do

```
alice.py
 -----------------------------------
| from bob import bobby             |
|                                   |
| def wonderland():                 |
|	return bobby() + ' loves Alice' |
|                                   |
| if __name__ == '__main__':        |
| 	print wonderland()              |
 -----------------------------------


bobby.py
 --------------------------------
| def bobby():                   |
|   from alice import wonderland |
|   return 'Bob'                 |
 --------------------------------
```

