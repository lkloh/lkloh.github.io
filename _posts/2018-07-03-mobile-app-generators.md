---
type: post
title: "Mobile Application Generators"
date: 2018-07-03
---

Summarized from [here](https://saschafahl.de/papers/appgens2018.pdf).

## What they are

Tools for partially of completely automating app development,
distribution, and maintenance.


## Pros

* Let developers focus on high-level functionality only,
  by abstracting away implementation details.
* Supports app lifecycle:
  core app generation, app compilation, dissemination, and distribution of patched verions,
* Support to make the app compatible with multiple architectures (e.g. Android and iOS).
* Support for user management, user login, data submission to backend servers

## Standalone frameworks

* Offer a code set of application functionality,
  refine by additional code by the app developer.
* Require programs to be wtitten in OS-agnostic languages (e.g. JavaScript and HTML),
  then packages the user-provided code with an execution engine into a native app.
* Plugins provided: inapp-browsers, advertisement, etc
* Examples: Xamarin, Apache Cordova


## Online Services

* For laymen who have never done app development before.
* Supports end-to-end prototype -> development -> distribution -> business analytics
* Enable app development using point-and-click web interfaces
* Developers add and interconnect UI elements representing application components
  (e.g. email forms, QR scanner, Facebook Like button).
* No need to write custom code.


## Developer-as-a-service

* Customer orders app creation
* App creation delegated to app developers who are given the customer's requirements
* Examples: CrowdCompass, QuickMobile







