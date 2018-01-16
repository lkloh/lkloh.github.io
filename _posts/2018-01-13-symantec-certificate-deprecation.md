---
type: post
title: "Symantec certificate deprecation"
date: 2018-01-13
---

Because of ongoing concerns with how Symantec issued SSL certificates over the last few years,
Google and Mozilla decided to deprecate Symantec certificates.
Problem was that Symantec certificates were so widely used that they couldn't just do it
all in one shot, or it would have severely disrupted many major websites.

In the end, Symantec handled operations of the PKI to DigiCert.

How it affects users:
* Certificates issued before Jun 2016 will expire in March 2018 - 2 months from now
* Certificates issued after Jun 2016 will expire in September 2018 with Chrome 70.
* DigiCert has been issuing certificates on behalf of Symantec since Dec 1, 2017.
* SSL labs have started issuing warnings when certificates issued by Symantec are in
  use on a website - to warn the owner and users that the certificate would be
  deprecated soon.
