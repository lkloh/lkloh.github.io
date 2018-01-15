---
layout: post
title:  "SSL Certificates"
date:   2018-01-05
---

There are several types of certificates that website domain owners 
could get from a Certificate Authority,
to indicate to users the extent to which they can trust their domain.

Of course, the Certificate Authority must be an organization that both domain owners
and users can trust as well.

## Domain Validated Certificate

The cheapest certificate offered by commercial Certificate Authorities,
which of course provides the lowest level of assurance.

Asserts that the domain has approved the certificate request,
usually done automatically. 

Not much value is provided if the domain visited has this certificate,
since they are so cheap and easy to obtain.
Having this certificate does not say anything about the security of visiting a site,
and one should never enter any personal information at a site that only offers this
type of certificate.

In fact, some [Certificate Authorities](https://www.digicert.com/dv-ssl-certificate.htm) 
don't even offer these certificates as they don't offer much value.

## Organization Validated Certificate

Required on commercial websites. 

The Certificate Authority will first verify that the organization that owns the domain
is a legitimate business by checking against government registries. 
Some form of human verification is usually involved.

## Extended Validation Certificate

Highest level of trust, required to establish trust for domains that
are used for ecommerce.

The Certificate authority is required to 
perform all the verfication steps as they do for Organization Validate Certificates,
and a [little extra](https://cabforum.org/extended-validation/).
The government ID of the business owning the domain and the
business's physical address is present in the certificate.


