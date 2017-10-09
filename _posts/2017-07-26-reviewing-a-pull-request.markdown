---
layout: post
title:  "Reviewing a pull request"
date:   2017-07-26
---

A pull request gives you a diff and list of files changed.
Here's a [guideline](http://blog.ploeh.dk/2015/01/15/10-tips-for-better-pull-requests/) 
for writine good pull requests,
and my summary

## What a reviewer must do

* Understand the requirement the pull request is supposed to achieve
* How does it fulfil the requirement?
* Make sure its high quality - what does this mean?

## How to write a good pull request

* Make it small - easier to understand context and reason about it
* Do one thing - doing too many things may need multiple reviewers, some of which are on vacation now
* Short line width - < 80 characters on a line if possible
* Make sure all tests pass - if it failed its probably your fault
* Add tests
* Make sure it builds
* Squash commits and force push if there are two many small commits that do very little 
	- less complicated things to care about
* Write useful descriptions and titles - give context about the goal of the pull request
* Have on-point commit messages - what changed and why, not how (it's in the modified code already)
* Add comments to guide the reviewer
* Use good English and grammer. Check for typos.
* Add screenshots/videos for front-end changes - if its mostly styling changes, rope in the designer as well
* Think about security issues - any vulnerabilities.
















