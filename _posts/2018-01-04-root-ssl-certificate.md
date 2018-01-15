---
layout: post
title: "SSL Root Certificate"
date:   2018-01-04
---

An SSL Certificate is a data file placed on a web server to connect a domain to a public encryption key to allow an SSL connection to be negotiated. 

Anyone can generate a public-private key pair and sign a new SSL Certificate,
then place it on the web server that hosts their domain (such as example.com).
But a user navigating to example.com using any major browser (such as Chrome/Firefox/Safari/Edge)
would not see the characteristic green padlock appearing in the browser window
that indicates that the website can be trusted.

In order for the healthy green padlock to appear,
the SSL certificate used must be be signed by a trusted Certificate Authority, 
such as [DigiCert](https://www.digicert.com/).
This means that the domain operator, users, and Chrome/Firefox/Safari/Edge, etc
all agree that the Certificate Authority can be trusted.

When a user's browser tries to validate the SSL Certificate of a domain
it is navigating to, in order to determine whether it can be trusted,
it will look at who issued the SSL Certificate.
If that certificate was issue by a trusted Certificate Authority, all is well.
Otherwise it will see if the entity that issued that SSL Certificate 
was signed by a trusted Certificate Authority...
and so on until it reaches the root of the certificate chain.
The certificate at the root of that chain is called the _root certificate_
and must have been issued by a trusted Certificate Authority.
