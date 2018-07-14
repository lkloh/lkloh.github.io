---
type: post
title: "Self-contained executables"
date: 2018-07-13
---

Summarized from [here](https://code.fb.com/data-infrastructure/xars-a-more-efficient-open-source-system-for-self-contained-executables/).

## The problem

Dsitributing dependent libraries and data files to thousands of machines at Facebook is a challenge,
as these machines will have varying configurations.
Copying the exact right library to each machine is hard.

## The solution: eXecutable ARchives (XARs)

A system to distribute self-contained executables containing data + dependency libraries
across large networks.

[Github](https://github.com/facebookincubator/xar/).

## What makes XARs suitable for large scale deployments

* Designed with the aim to distribute and execute large Python applications
* Compatible with open source Python ecosystem
* Can be run anywhere on the filesystem; no need for virtual environments
* Single highly compressed files with all executable dependencies
* Execute at the same speed as natively installed applications

## How they differ from othe self-contained executables

* No explicit decompression
* Squashfs files that mount themselves when executed, unmount after some idle timeout period
* Data is compressed more than a zip file
* Only portions needed are decompressed on demand


