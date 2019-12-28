---
type: post
date: 2019-12-27
title: Software Development Processes Introduction
---

Summary of the class [Software Development Processes and Methodologies](https://www.coursera.org/learn/software-processes/supplement/51Rwg/welcome-to-the-course) on Coursera.

The class is about software development processes,
which are usually codified 'common sense'.
Howeverm software is so complex that it's hard to see when mistakes have been make, unlike a civil engineering project where it's obvious if a building has a massive crack in it. Lots of projects have failed in the past, some during the requirements gathering process, some in the beta rollout.

When building a piece of software, the waterfall method for a large project taking 1-2 years is like this:
1. gather requirements - what are we building?
2. Architect the system - what components are we gonna build?
3. Code the different components, write unit tests for them
4. Do integration testing of all components together
5. User Acceptance Testing - make sure users like what the devs have done
6. Production release - users use the product
7. Maintainance - fix bugs and change things in response to user feedback.

The problem with waterfall is that its hard to predict requirements of a project years in advance, devs can misinterpret requirements, and integration issues can go undetected. People came up with many variants of waterfall testing to fix this, but one new method has become popular.

The Agile method is not a model of how software is built, but a mindset.
Instead of 1 year cycles, we build and test things in small cycles 
to learn from users early, and tweak things after each small cycle.
It uses continuous integration, so once a dev has submitted a pull request,
it gets integrated with the rest of the system, all automated tests run,
and the PR is automatically deployed. This has been shown to be effective on
relatively small projects for teams of maybe 10 people,
but the jury is still out for much larger (think 10000 people) teams.

An example of the process is when Zappos wanted to sell shoes online,
a novelty when the company was founded.
To check whether people would buy shoes online, they just
built a website to let people order shoes online, and manually
bought shoes from a store and shipped them to the customer when a customer
places an order. They only started building out scaling processes after
they proved that people were willing to buy shoes online.

Part of the Agile process also involves getting devs interested in the 
overall outcome of the project, not just their personal output.
This lead to other evolving processes, like caring about people's
motivation, psychological safety, and growth mindset.
