---
layout: post
title:  "Your side effects are someone else's main business"
date:   2017-10-26
---

[This article](http://queue.acm.org/detail.cfm?id=3099561) discusses 
how we do things for one main purpose,
but whatever we do has side effects for someone else.

Example: when I sign in to a shared computer cluster
to mine Bitcoin, mining Bitcoin is my goal.
However, a side effect is that the cluster logged my session.
Someone else's main job duties are to ensure the logging script
works accurately most of the time,
and conduct regular audits to make sure that users are behaving appropriately.

## Side effects can persist even if the act causing them is cancelled

There is one dress left in an online store at 1pm.
Jane and Mary both try to buy it at the same time.
Mary thinks she would look perfect in it,
while Jane just wants to try it out.
Jane's order gets placed first, 
so Mary's order fails as the last dress was claimed by Jane first.

At 2pm Jane changes her mind and cancels the order.
Eve sees that the dress is available and buys it.
Mary isn't around to buy it right now as she is on a train with no wifi.

Now the side effect of Jane buying the dress at 1pm
is that Mary cannot have a dress she really wants.
Though Jane ended up not buying the dress as she cancelled her order,
the side effect _persisted_.

## Don't worry too much about side effects in general

Unless you're the one implementing one of functions in the interface.

If you're the one doing implementation,
absolutely think about the expected side effects and their severity.
Part of your job is to have good system design.

If you're just relying on the abstraction someone else already performed,
chill out. You'll go crazy thinking about all possible scenarios
that can happen as a result of your actions otherwise. 
System interaction is just too complicated.
