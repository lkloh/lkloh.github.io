---
type: post
title: "Performance impact of SSL"
date: 2018-01-19
---

Summarized from [here](https://www.maxcdn.com/blog/ssl-performance-myth/).

## Computational resources affected

Opening the SSL connection is the most resource intensive
as it requires asymmetric encryption to establish 
a symmetric session key.
Worst case scenario is to increase CPU usage by 5%.

To increase the speed of computations when using SSL,
consider using Advanced Encryption Standard (AES),
which uses inbuilt instructions in hardware to support
faster SSL connections.

## Impact on network performances

The initial connection does cause performance to take a hit,
but subsequent encrypted traffic does not impact the performance by much.

False start performs encryption in parallel during a TCP handshake
to transfer data more quickly.
A normal TCP handshake requires three steps to establish a connection:
(1) SYN (2) SYN-ACK (3) ACK.
Normally they are performed in parallel, but False Start
starts encrypting date to be sent the moment step 1 (SYN) is sent to the server to save time.

Caching keys and connection information on the client and server
reduces the number of round trip connections over the network and thus saves time,
though it requires the server to be able to cache a potentially large number of sessions.
To avoid needed to cache so many sessions, the storage for the session 
could be moved entirely to the client.
The server uses a private key to encrypt the session information on the client
and resumes the session if it verifies that it has previously trusted this client.


