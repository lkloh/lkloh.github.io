---
type: post
title: "Kestrel Message Queue"
date: 2018-08-04
---

## Kestrel: the message queue server

Built by [Twitter](https://blog.twitter.com/official/en_us/a/2009/building-on-open-source.html)
when the engineering team realized that no open source offerings were capable
of handling the scalability requirements of their service.

## How Kestrel was used by Twitter

Kestrel was used to asynchronously connect many of the services and functions at Twitter.
_Was used_, as Twitter eventually outgrew Kestrel as well.

For example, when users update,
any tweets destined for SMS delivery are queue in a Kestrel Message Queue.
The SMS service then reads tweets from the Kestrel Queue,
and communicates with the SMS carriers for delivery to phones.
In this way, the implementation isolates the SMS delivery from the rest of the system,
so it can be operated independently.






