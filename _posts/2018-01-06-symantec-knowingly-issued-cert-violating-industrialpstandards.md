---
layout: post
title: "Symantac knowlingly issued a certificate violating industrial standards in late 2013"
date:   2018-01-05
---

In late 2013, one of Symantec's customers that make devices that communicate to web servers
needed to renew their SSL certificate with Symantec.
Because hardware is not as easily upgraded as software,
they needed Symantec to reissue the certificate with a 1024-bit public encryption key,
instead of a 2048-bit public encryption key as required by
the CA/Browser Forum Baseline Requirements,
which had changed since the last time the customer had renewed their certificate.

Symantec agreeded and renewed the certificate with a 1024-bit public key 
(instead of pushing back and insisting the customer upgrade their decives
to enable a 2048-bit public key for SSL connections), because
* The customer's made hardware which is difficult to upgrade quickly,
  and their business would have been severly disrupted without the renewal
* They believed the 1024-bit certificate would have posed little risk to browser users,
  and furthermore the certificate was not intended to be used by browsers anyway,
  as the customer's produces communicated directly with web servers instead.

Some browser vendors were [pissed](https://bugzilla.mozilla.org/show_bug.cgi?id=966350) because the certificate issued
still asserted that the customer complied with all CA/Browser Baseline Requirements,
though it clearly did not.



