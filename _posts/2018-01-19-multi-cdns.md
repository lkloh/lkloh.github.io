---
type: post
title: "Multi-CDNs"
date: 2018-01-19
---

Summarized from [here](https://www.webopedia.com/TERM/C/CDN.html) and
[here](https://www.maxcdn.com/blog/multi-cdns/).

## What is a Content Delivery Network (CDN)?

Networked servers that deliver content to end users (people using a browser to browser the web).

## Why are networked servers needed, instead of just one server?

So that the servers can be in different geographical locations,
to deliver content more quickly to users in their locale.
Many used by websites with lots of traffic and international users.

## How it works

* Client visits the webpage, making a request for its content
* Originating site's server sends the request to the 
  CDN server nearest to the client geographically, which pulls the cached content request and servers it up quickly.
  Or maybe it pulls fresh content from the originating site's server if necessary/

## Why do companies pay for CDNs

* Faster page load
* Less bandwidth consumption 
* Protection against network spikes
* Security - some CDNs block spammers 

## Why use multiple CDNs?

A.k.a multiple CDN providers - CDNs owned by several different companies.

* Companies with large user bases in North America and the Middle East
may want a CDN with the headquarters in North America,
and another in the Middle East, so that the CDNs they used
are targeted for the particular regions they serve.
* Some CDNs are better for websites that offer streaming (e.g. Netflix),
  while some are better for images (e.g. Instagram).
* Putting eggs in differen baskets - defense agains a CDN provider
  shutting down, hacked, having its servers hit by a hurricane, etc.
