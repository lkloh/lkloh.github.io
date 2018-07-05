---
type: post
title: "The security impact of online app generators"
date: 2018-07-02
---

[This paper](https://saschafahl.de/papers/appgens2018.pdf) studies whether
the increasing number of mobile apps automatically created by online application generators (OAGs)
has caused security vulnerabilities in the overall all ecosystem.
While OAGs lower the bar for the technical skill needed for app development,
their pervasive usage can have a negative influence on the security of generated apps.

The paper studies how commonly used OAGs for Android,
and found that at least 11% of the ~2 million free Android apps from Google Play
were created by OAGs.
They also found that the app general model is based on boilerplate code 
prone to reconfiguration attacks in some of the OAGs,
and that the boilerplate code also includes common security issues such as 
code injection vulnerabilities and insecure WebViews.

To address this issue, a short term stopgap measure would be to
inform OAGs about security issues that are discovered, and ask them to fix the issues.
A long term solution would be for the OAG community to investigate 
how App Generators are built and require particular security standards for them,
as a single security vulnerability in an OAG has an amplification effect
that causes and overall net negative in the app ecosystem.


