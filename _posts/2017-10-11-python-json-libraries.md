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

According to the post `ujson` is the fastest but can be buggy. `json` is a lot more through. 

Json is used to send information over a network, so the amount of information can get quite large. Thus using a quick library can be important. 

Libraries working quickly for big files work badly on small files and vice versa. So chose the library that fits your expected use cases best.

