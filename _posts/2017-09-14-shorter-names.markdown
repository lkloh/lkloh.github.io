---
layout: post
title:  "Shorter names in programs"
date:   2017-09-14
---

Magic numbers are not good for maintainance. Clearly
```python
def sell(n):
    while n >= 7:
        n--;
        sell_a_crate()
```
doesn't explain what `7` represents.

It would be better to do something like:

```python
num_crates_to_keep_for_personal_use = 7

def sell_produce_we_will_not_use(n):
    while n >= num_crates_to_keep_for_personal_use:
        n--;
        sell_a_crate_of_extra_produce()
```
for long term maintainence.

But that results in a different problem:
names that are too long decreate readability as well.
The human eye can only take in so much.
This [StackOverflow](https://stackoverflow.com/questions/1017624/when-is-a-function-name-too-long) 
post has a long discussion, but in essense it boils down to:


* Names should be <= 40 characters, 
    more than that makes it hard to digest when looking
    at the function from a screen.
* Names should describe the what the function/variable is used for.
* If its not possible to fulfil the above two, you need to do some refactoring.

So something like
```python
n_crates_to_keep = 7

def sell_excess_produce(n):
    while n >= n_crates_to_keep:
        n--;
        sell_crate()
```
would be better.

