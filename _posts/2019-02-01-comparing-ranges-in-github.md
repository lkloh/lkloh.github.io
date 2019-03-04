---
type: post
title: "Comparing ranges in Github"
date: 2019-02-01
---

Edited from [here](https://stackoverflow.com/questions/29518780/way-to-compare-range-of-commits-in-pull-request-on-github).

I made 5 commits in a PR on github,
and asked for a review.
To address the feedback, I had to make 3 new commits.
To get the PR approved, I needed to go back to the reviewer and tell him what the new changes were.

To do this, I found the last commit that had already been reviewed and clicked its hash link to get
```
http://github/my-repo/pull/27/commits/a54328a9f7ae81fd14f6466b48dbef8476281cf5
```

I changed `commits` to `files` and added `..HEAD` to the end of the url to get
```
http://github/my-repo/pull/27/files/a54328a9f7ae81fd14f6466b48dbef8476281cf5..HEAD
```
and got all the changes from the 3 new commits, so I sent that link
over to the reviewer to explain he just needed to examine these new changes.


