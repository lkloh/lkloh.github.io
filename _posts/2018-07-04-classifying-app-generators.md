---
type: post
title: "Classifying app generators"
date: 2018-07-04
---

[The authors of this paper](https://saschafahl.de/papers/appgens2018.pdf)
did a study on how online app generators could spread security vulnerabilities
through the app ecosystem.

To identify common app generators,
they used Google search for that.

Steps:
* Simulate a user searching for an app generator,
  by searching for terms on [Google|Quora|Appindex|Businessnewsdaily|Werockyourweb] for
  ["app maker android", "android generate app", "business free diy mobile",
  "android app generator"], etc
* For each result, they selected the top 5 hits after removing duplicates

Classification:
* Freeware - free app generators
* Multi-platform support - develop on one platform, automatically
  generate native apps for the rest
* Components - app generators offering extra services such as ads,
  app analytics, user management, crash reporting
* Publishing - app generation + distribution to potential users

