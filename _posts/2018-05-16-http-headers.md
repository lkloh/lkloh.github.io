---
type: post
title: "HTTP Headers"
date: 2018-05-16
---

Summarized from [here](https://www.fastly.com/blog/headers-we-dont-want).

## Some things they do

* Control how caches/browsers process a site's content

## How they can get out of hand

* When used wrongly, add overhead to page load time
* Displays too much information about your servers and make them easier to attack

## Commonly used headeers

* `content-type`
* `content-length`

## Important but less widely used headers

Improve security
* `Content-Security-Policy`
* `Strict-Transport-Security`

Improve performance
* `Link rel-preload`

## Popular headers that are not useful

About your choise of server software
* Example: `server` | `x-powered-by` | `via`
* No one needs to know, especially not malicious hackers
* Not required by protocols

Deprecated standards
* Headers that outlived their usefulness - software gets outdated really fast without frequent maintainance!
* `P3P` | `Expires`

Debug data
* `X-Cache` | `X-Request-ID` | `X-ASPNet-Version`
* Headers not in any standard, that are not required by browsers but may be useful to developers
* Find a way to turn them on in development mode only, not production

Misunderstandings
* `pragma: no-cache` was deprecated before the turn of the millenium, 
  but is commonly thought to be required in response headers still.
  It was originally only intended for requests headers.
  You should use `Cache-control: no-store, private` to make sure something is not cached
* `X-Robots-Tag` is only used by crawlers such as Google's bots,
  so it should not go into headers targeted at a browser.
* In a request, a `host` header makes sense, but not in a response.



