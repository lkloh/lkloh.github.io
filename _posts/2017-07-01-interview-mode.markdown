---
layout: post
title:  "Interview mode"
date:   2017-07-01 01:57:45 -0700
categories: technical interviews
---

The last post I wrote was about using [Pramp](https://pramp.com/#/) 
to prepare for technical interviews
with other people who are also doing the same.

Pramp was awesome for preparation of course, 
because I could schedule interviews every two hours. 
Only sad thing was the interviews could only be scheduled between 11am - 11pm
(I was on the East Coast in Pittsburgh),
in other to ensure that I had a peer to be matched too.
It's likely because most of the users are in California,
where the headquarters of many tech companies are. 
While I did get one onsite interview with a hiring manager from Amazon,
it's not built specifically for the purpose of matching users
to places they may be interested in working at. 

Now let's talk about [interviewing.io](https://interviewing.io/),
which matches people preparing for technical interviews,
to experienced engineers to give them proper feedback. 
Both parties are anonymous during the interview session
to remove as much unconscious bias as possible.
After the interview, if both parties want to unmask their identities,
they can do so. 
If you do well, you might get invited to onsite interviews
at the places where those engineers work.

I tried siging up for it while job hunting, 
but got an automated message stating that they were still in beta
and that I would be up later.
So I emailed `hello@interviewing.io`, 
and one of the cofounders got back to me and let me onto the platform immediately.
It seems that for small startups of <10 people,
the cofounders themselves are often monitoring the emails coming in from users,
so asking for something might actually be pretty effective.

Well, I tried to book a slot, but the earliest one was a week later.
So I continued practising with Pramp until then.
The first interviewer gave me a pretty tough problem 
(that could be solved using a graph traversal algorithm)
that was a scaled up version of one of the problems I got on Pramp,
and I took almost 90 min (a.k.a. double the time of a regular 45 min long interview session)
to solve it. Even then, I'm not sure if I got a complete working solution,
but the interviewer was sufficiently impressed to ask to be introduced to me. 

I had to wait another week to book the next interview.
I got a generic dynamic programming question at that one,
which I should have known how to solve immediately, but didn't. 

So I had to wait another week to book another interview.
I was getting annoyed at this point,
because the site said that it was meant to help people practice their
technical interviewing skills,
but waiting a week between each practice isn't very helpful.
At the third interview, I got a pretty simple question that was
a scaled down version of a real world problem
- how would one generate a unique id for each additional machine added to a data center
in a scalable way? 

Perhaps I practised technical interviews a bit too much.
For that question, I stated the obvious:
to have a global counter tracking the highest numerical id
of all the machines in the data center.
When a new machine is added, increment the global counter by 1
and set that to be the unique id of the new machine. 
I figured we wouldn't run into integer overflow problems
on a modern 64-bit machine because data centers are not that large right now.

I should have stopped there.
But instead I tried to be smart and talk about further ways of optimization,
because the problem reminded me of some hacky technical challenge problem
I had seen in the past.
The interviewer actually didn't like that,
because he advised me to focus on demonstrating real life engineering skills
instead of trying to impress people with how clever I was theoretically. 
He even said he could tell that I was in "interviewing mode" then,
and advised me to try and act more like a genuine human instead of some
algorithm solving machine. 

I'm guessing he works for a relatively small start-up.
At most bigger companies, being in "interviewing mode"
is exactly what you want to be at to get the job. 
Because these places have the resources to train you from scratch
and just care that you know the fundamentals well.

At smaller start-ups I interview at, 
I got a lot more focus on real skills that I would be 
expected to apply if I actually got the job and started working there.
Things like system design, or code refactoring,
or HTML/JavaScript specific exercises. 

It's hard to remain in interview mode for long once you have a job,
because the types of traditional algorithm challenges given out at
large companies tend to be far removed from what a software engineer really does.
Soon after accepting the offer from Mixpanel, 
I scheduled another practice at interviewing.io just to see how I would do.
The interviewer told me I "needed more practice".



















