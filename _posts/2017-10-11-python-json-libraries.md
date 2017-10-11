---
layout: post
title:  "Python Json libraries"
date:   2017-10-11
---

[This post](http://artem.krylysov.com/blog/2015/09/29/benchmark-python-json-libraries/) 
explains which json library a Python user should use.

The libraries, which are supported by Python 3:
* json
* simplejson
* ujson
* python-rapidjson

According to the post `ujson` is the fasted but isn't always accurate.
If everything must be accurate, use `json`. 

Json is used to send information over a network,
so the amount of information can get quite large.
Thus using a quick library can be important. 

According to this other post,
no json library is obviously better than the others.
Which probably explains why so many exist to solve 
almost the same problem.
Libraries working quickly for big files worked badly for small files and vice versa.
So chose the librarie that fits your expected use cases best.
































