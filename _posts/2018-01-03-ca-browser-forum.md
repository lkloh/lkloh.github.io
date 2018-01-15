---
layout: post
title: "Certificate Authority/ Browser forum"
date:   2018-01-03
---

Known as the [CA/Browser Forum](https://cabforum.org/),
which counts as members Certificate Authorities and Browsers,
with the aim of proposing industry best practices to enhance online security.

Summarized from [here](https://www.globalsign.com/en/blog/what-is-the-ca-browser-forum/).

## Certificate Authorities 

Responsible for following industry standards when issuing SSL certificates.
Their primary job is to vet requests for SSL certificates to ensure the owners of 
a domain requesting a certificate is engages in legitimate activities,
instead of trying to harvest users' credit card numbers.

So they have a very important job to make sure that the entity that the issue
a certificate to are good actors.


## Browsers

The mode through which most online users used to visit websites,
many of which may be malicious.
Its important for a browser to display warnings if a user has navigated to
an untrusted site - perhaps the user would reconsider
signing up for an account of handling out their credit card information.

## How to enhance trust in a certificate

Check that the entity requesting a certificate for a particular domain
is a legitimate business registered with the government,
and potentially interviewing representatives of the entity in person.

Set a certificate to be valid for a limited period of time (e.g. 2 years).
The entity must recerify every few years to incentise them to
upgrade their technology to the latest industrial best practices.


