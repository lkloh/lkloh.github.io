---
type: post
title: "Are two masked mobility records created by a single user, or different users?"
date: 2018-07-15
---

Summarized from [here](https://arxiv.org/abs/1702.06270).

One you have an answer to this question, you can recover a user's mobility record
from an anonymized dataset.

## Users don't move around much at night because they are sleeping

Or at home resting, you get the idea.

Mobile users usually don't move around much at night
- >90% of the nighttime records are in the same location, probably their home.

This fact can be used to estimate a mobile record's next location,
and associate them to belonging to the same user.
Thus it is easy to figure out where a user is at night.

## Users move around continuously during the day

One can estimate a user's next location based on their current one.

The authors did this by using a velocity model to estimate the next location of a user,
and associate unassigned location points with nighttime locations,
and thus recover the whole trajectory for each day.

## Humans are creatures of habit

A single person's trajectory during a 24-hour period is very regular for
his own day-to-day, but highly unique from someone else's trajectory.

One can associate several users' mobile records across days by measuring their similariy,
and associate highly similar records across days with the same user.





