---
type: post
date: 2020-01-15
title: "Why Github recommends clone repos with HTTPS over SSH"
---

https://help.github.com/en/github/using-git/which-remote-url-should-i-use

* HTTPS is easiest to set up on most platforms.
* HTTPS is easier to set up for a new user. With SSH you need to generate an SSH keypair
and add the public key to your GitHub account. 
Not everyone wants to do this.
* HTTPS is a port open in all firewalls, while SSH can be blocked by a firewall.
This makes it easier to access a GitHub repository with HTTPS vs SSH.



