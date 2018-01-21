---
type: post
title: "Formal methods to increase reliability in the industry"
date: 2018-01-01
---

[Coq](https://coq.inria.fr/) is a proof assistant designed to help
academics write specifications and prove them.
It's not as easy to prove that `1 + 1 = 2` is true in Coq as it should be.
But still its a very important part of formal verification,
which aims to verify a system under certain assumptions.
As long as those assumptions hold, the system has no bugs.

Problem is that formally verifying the system in Coq is a lot of work.
Think about verifying something like Linux.
No one is going to do it because the amount of time and energy wouldn't be worth it at all.
Even if it means a bug free system.
Even if some bugs can [cause a lot of money to be lost](https://www.around.com/ariane.html).
The delay to projects and manpower required doesn't make it worth it.

Well, not using Coq anyway.

Amazon Web Services (AWS) has had a lot of success using TLA+,
a formal specification language, to find subtle bugs in the very complex systems
they build and maintain.
Essentially, AWS has so many incoming events every second that
even cases which are "unlikely to happen" will start happening often enough
to affect paying customers and make them unhappy.
The usually QA processes and unit testing for common scenarios just isn't enough
to provide the guarantees that AWS needed, 
and furthermore it was too difficult to think of all potential ways
an implementation could be problematic.

Using TLA+ helped fix some of the problems AWS faces.
They needed a precise design of what they wanted to find subtle bugs,
and also check for errors in the design while the design process was happening,
not just during implementation in an imperative language like C++.
They also needed something that was easy to learn,
not something that takes a PhD student 5 years to master.

Turns out TLA+ had most of the things they were looking for,
describing all possible ways a system could execute,
with different levels of abstraction, and usually taking about
~3 weeks for a new grad to become effective with.
TLA+ has been used on many complex real world systems,
so its not just useful for proof-of-concept research work.

One problem TLA+ does not solve is checking for slow response times,
as AWS's servers do not support real time scheduling guarantees,
so they have to used other techniques to catch when slow response times occurs.

Summarized from [here](http://lamport.azurewebsites.net/tla/formal-methods-amazon.pdf).






