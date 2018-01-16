---
type: post
title: "Federal PKI is untrusted in browsers"
date: 2018-01-06
---

The US Government has a PKI called the Federal PKI (FPKI),
which is apparently very complicate.
Thus many major browsers do not include the FPKI in their root store
as it is so complicate that it is too much work to bring it in line with their policies.

Apparently Symantec had a cross-sign for one of the Federal CA,
meaning Symantec would be responsible for all certificates issued in the FPKI 
as it now becomes the root trusted CA for browsers that have Symantec as a trusted CA.
Thus Symantec assumes responsibility for making sure the FPKI
adheres to all CA/Browser Forum policies.

When notified that Symantec signing the Federal CA would cause browsers that used
Symantec as a trusted CA to show the federal websites as trusted,
Symantec decided to let the certificate expire, instead of revoking it immediately.
