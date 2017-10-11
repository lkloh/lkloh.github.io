---
layout: post
title:  "`list.sort()` vs `sorted(list)`"
date:   2017-09-18
---

## list.sort() sorts the original list in place

* Space efficient 
* May work [a bit faster on large lists](https://stackoverflow.com/questions/22442378/what-is-the-difference-between-sortedlist-vs-list-sort-python),
	but explicitly choose this due to increased speed would be premature optimization.

## sorted(list) preserves the original and returns a new sorted list

* Use this if you need to preserve the original
* Used to sort an iterable that is not a list

## Conclusion

Pick the one to use based on whether you need to preserve the old list or not.



