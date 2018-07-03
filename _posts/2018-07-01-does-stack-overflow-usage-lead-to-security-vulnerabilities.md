---
type: post
title: "Does Stack Overflow usage lead to security vulnerabilties?"
date: 2018-07-01
---

[This paper](https://arxiv.org/pdf/1709.09970.pdf) studies whether the Java platform and
third-party libraries that are intended to help developers write secure code,
actually cause security vulnerabilities when misued.

The authors found that many Java devs use the security features provided
by Spring security, a third-party framework for secure enterprise applications
which can be challenging to use.
There are lots of security vulnerabilities in the code of accepted answers
on Stack Overflow, 
such as using insecure hash functions (e.g. MD5),
and breaking SSL security by bypassing certificate validation.


In conclusion, the authors believe that this is due to a gap between
security theory and application.
Also, many developers don't know about best practices for security,
and one wrong accepted answer on StackOverflow can propagate through the 
community quickly and cause vulnerabilities... everywhere.

As workforce retraining to correct security issues can take
a while to take effect "ship fast and break things",
the authors suggest building semi-automatic tools to detect security bugs
as an immediate next step.

