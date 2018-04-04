---
type: post
title: "How Mailrelay manages email bounces"
date: 2018-03-28
---

[Mailrelay](https://mailrelay.com/en) is a service for sending email campaigns for marketers.
So there may be several thousand emails going out to a list of potential customers for any given campaign.

To select a list of email addresses a campaign is to be sent to,
a Mailrelay user needs to click on the file with email address using the "Import" button.
While the emails are being loaded to Mailrelay's platform,
the system inserts the emails into the customer's account.
While the insert takes place, some emails that have cause bounced email in the past may be detected.

The detection of emails that caused bouncing in the past is aided
by Mailrelay's database of permanently bounced emails, which is shared by all customers
(customers cannot see other customers' emails using the shared database).
The shared database aids detection of invalid email addresses.

If a bounce was due to an inbox being full/ recipient server failure,
it is a _soft bounce_ (recipient domain returns error 400),
and Mailrelay will retry the sending every 15 minutes
for a period of time, making a best effort to deliver the message.

If a bounce happened as the email address was wrong/ expired,
this is a _hard bounce_ (recipient domain returns error 500).
Mailrelay adds it to its shared  database of bounced emails from all customers.

This crowdsourcing allows Mailrelay to send a higher percentage of emails
only to valid email addresses, to ensure a higher quality of sent messages
reaching only actual human beings. 
In this way they protect their customers' domain reputation by only sending email
to (mostly) legitimate addresses.

