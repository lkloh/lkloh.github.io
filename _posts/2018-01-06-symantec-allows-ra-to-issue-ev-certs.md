---
type: post
title: "Symantec allows its partner Registration Authorities to issue Extended Validation Certificates"
date: 2018-01-06
---

Symantec's four Registration Authority (RA) partners are technically capable
of issuing Extended Validation (EV) certificates,
though these RA partners do not perform EV audits.

Apparently the RA partners issued EV certificates on several occasions, which is problematic as
(1) They are not able to perform the required audits to issue an EV certificate
(2) Due to (1), they should not be technically capable of issuing EV certificates in the first place.
    This violates the principle of least control.
(3) Symantec did not disclose the issuances when they discovered them to major browser vendors
(4) Symantec did not take immediate steps to stop the issuance of EV certificates from
    the RA partners upon discovering the RAs had done so.

So Mozilla was pissed. Read about it [here](https://wiki.mozilla.org/CA:Symantec_Issues).
