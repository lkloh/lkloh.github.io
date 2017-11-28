---
layout: post
title:  "Rate limit your user facing apps/apis"
date:   2017-10-09
---

Rate limiting is done for a reason: because it has caused trouble in the past.
This article describes [more](https://blog.codinghorror.com/rate-limiting-and-velocity-checking/),
and here is a summary:

## Why you must rate limit your website's UI

* _Rate limits are there due to unpleasant prior experiences._
Example: A restaurant has a sign forbidding dogs. It's not because the owner hates dogs, its because dogs have caused trouble in his restaurant in the past and he's learnt from painful experience. Otherwise he would have a sign saying "no snakes allowed" since most people (including him) probably don't like snakes either.
* _It is necessary._ 
Example: An unlimited login entry is really dangerous - with enough time someone with a decent a password cracker could probably get in. Block login attempts after a certain number of failures, even if it means locking out the real account holder who just forgot his password as well.
* _Even innocent actions in large quantities can cause harm._ Too many users going onto a store's website to buy a dress Kate Middleton wore have cause a shopping site to crash, which is undesirable.

## Ways to implement rate limiting

* Per user/ API key - `n` actions / minute - problematic if a user creates many fake accounts
* Per IP address - problematic if there are many users behind a proxy with one IP address
* Per action, only `n` actions of any type (e.g. create new account) allowed on the site per minute - used for admin actions which are typically few, but problematic if a malicious attacker gets admin rights

## Very effective defense against many different types of attacks

* First line of defense - writing a bot to DDOS a website is easy, using assembly code to construct a return-to-libc attack is usually harder and needs more specialized (i.e. rare) knowledge
* Can mitigate/defeat a large class of attacks