---
layout: post
title:  "US Economic sanctions and how it affects who can view your website"
date:   2017-10-31
---

The U.S. sanctions several countries for various reasons
that are beyond the scope of what I need to know for the job that I do.
This involves commerial transctions,
some of which take place over the internet.
U.S. Companies are required to obey these sanctions.
Failure to obey the sanctions may result in a large fine,
and potentially other negative consequences.
Some of the countries that have been sanctioned now/in the past are:
Cuba, Syria, North Korea, Syria, Burma.

Some consequences are that educational websites
such as Coursera get [blocked in Iran](https://www.thedailybeast.com/how-american-economic-sanctions-are-hurting-innocent-students-in-iran-cuba-and-sudan).
So Iranian residents can't view the content provided by Coursera.

If you're a U.S. based service provider,
[here](https://www.sitepoint.com/how-to-block-entire-countries-from-accessing-website/)
are some ways to comply with U.S. sanctions:

Get someone else to do it for you:
* Use a hosting company that does the blocking for you.
For example, [IBM's SoftLayer](https://knowledgelayer.softlayer.com/faq/softlayer-network-wide-ip-blocking)
blocks IP addresses associated with sanctioned countries.
The list of IP address to be blocked is obtained from MaxMind.
* Use a CDN such as Amazon's CloudFront,
	which lets you choose a list of countries to block access.

Do it yourself:
* Use a [free API](https://freegeoip.net/?q=2602:306:83b7:c0a0:bdb8:9e0a:12fa:c87b) 
	to find out where an IP addresses associated with a request came from,
	and block if it comes from a sanctioned country.


