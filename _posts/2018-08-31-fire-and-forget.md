---
type: post
title: "Fire and forget"
date: 2018-08-31
---

A form of asynchronous communication, where a sender sends a message to the recipient,
and continues operations without waiting for a response.
Stateless, hence the phrase 'forget'.
Useful when building a scalable messaging system as you don't need to store any state.
Only problem is that there is no error handling possible as the sender does not
wait for any acknowledgement from the recipient.

