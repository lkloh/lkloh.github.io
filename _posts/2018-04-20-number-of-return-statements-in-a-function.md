---
type: post
title: "Number of exit points in a function"
date: 2018-04-20
---

What's better?

```py
def recommend_beauty_products(person):
  if is_female(person):
    return {
      'body': ['Moisturiser', 'Soap'],
      'clothes': get_recommended_clothes(person.height, person.weight),
      'foundation': ['Lancome', 'LOreal', 'Maybelline'], 
      'hair': ['conditioner', 'shampoo'],
      'lipstick': ['Glitter', 'Matte', 'Metallic', 'Natural'],
    }
  else:
    return None
```
which has two exit points, or

```py
def recommend_beauty_products(person):
  if not is_female(person):
    return None
  return {
    'body': ['Moisturiser', 'Soap'],
    'clothes': get_recommended_clothes(person.height, person.weight),
    'foundation': ['Lancome', 'LOreal', 'Maybelline'], 
    'hair': ['conditioner', 'shampoo'],
    'lipstick': ['Glitter', 'Matte', 'Metallic', 'Natural'],
  }
```
which has a function guard that essentially stops execution when a
crucial condition does not hold?

Returning early also prevents deeply nested `if` statements,
which enhances readability.

Read more [here](https://www.tomdalling.com/blog/coding-tips/coding-tip-have-a-single-exit-point/)
on the case for having a single exit point.


