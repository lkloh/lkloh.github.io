---
type: post
title: "How Instagram moved to Python 3"
date: 01-23-2018
---

Summarized from [here](https://thenewstack.io/instagram-makes-smooth-move-python-3/).

## Why did Instagram use Python in the first place?

When they were a small startup, the used Python because it was a simple
language, so the engineers could focus on getting a product to market
quickly instead of learning the nuances of a hard language.

## Why did Instagram decide to invest in Python 3?


* I/O Scalability: Instagram's user base kept growning (400 million users now)
and speed was very important. At some point more money was being
spent on AWS servers than product development into new features.
* Familiarity to developers: They considered using a new stack, but decided to keep Python/Django as most of the engineers at Instagram were most familiar with it and using a different stack would require lots of ramping up.
* Python 3 has many improvements over Python 2, such as increased speed and typing.

## How did they make the move?

1. Replace Python 2 packages with Python 3 packages, also deleting unused ones (3 months)
2. Unit testing (2 months)
3. Slow rollout (4 months)

## What did they find important to the successful migration?

Iterating in small steps at all times.

## How happy are they with the move?

Happy,
1. 12% CPU savings on WSGI/Django
2. 30 memory savings on celery



