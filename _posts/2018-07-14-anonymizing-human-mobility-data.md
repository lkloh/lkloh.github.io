---
type: post
title: "Anonymizing human mobility data"
date: 2018-07-14
---

Summarized from [here](https://arxiv.org/abs/1702.06270).

TL;DR: Humans are creatures of habit, and thus predictable,
so anonymizing their data before publishing it usually doesn't work well.

## How human mobility data is collected

Through cell networks and mobile apps, before being publicly released. 
* Wechat in China has a [public interface](http://admin.wechat.com/wiki/index.php?title=Callback_Data_API)
  for obtaining real-time population information.
* Apple updated it privacy policy to make users allow for sharing mobility data 
  with its partners. 
* Orange (mobile operator) made many of its cellular accessing records available to researchers.

## Attempts at preserving the privacy of mobile users when releasing data

People are concerned about their privacy, so data owners
usually publish aggrgated mobility data only.
For example, the number of users covered by a cellular tower at a particular time.

Aggregate data is useful for epidemic controlling, transport scheduling, and business intelligence,
while still preserving individuals' privacy.
At least, that seems to be what some people believe.

## Unmasking individuals from a statistically aggregated mobility dataset.

The paper presents a way to unmask individuals form an anonymized dataset.

A single person's mobility patter is highly regular,
so their trajectory is very predictable.
For example, most people usually commute between the home and office at the 
same time on a weekday.

The authors found that by figuring out whether two masked mobility records
are created by a single user or different ones,
they can recover a single user's trajectory easily. 

There are several ways help finger a user more easily
* Humans usually have only a few places (home/school/bar) that they hang out in regularly
* Humans usually stay at home at night, and move in the daytime
* The way people walk/move varies a lot from person to person













