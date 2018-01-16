---
type: post
title: "Breaking Captcha"
date: 2018-01-14
---

[Captcha](https://www.google.com/recaptcha/intro/) is supposed to help
defend websites agains automated bots and spammers.

Well its not always that effective.
There's an entire industry that uses automated humans in style similar to
Amazon Mechanical Turk to get humans living in areas with a low cost of living
to break captchas. There are fancy [APIs](https://anti-captcha.com/mainpage) for that
which have great marketing strategies an testimonials from their employees
about how they have used their salary to feed their families.
Its all very cheap, starting from USD $1 to solve 1000 captchas.

Also, deep learning researchers have found that they could
make use of Google's reversed image search to label a Captcha image,
then use that work tag and some open source machine learning libraries
to build a completely automated tool to solve captchas with a 70% success rate.
So essentially they used one Google product to break another Google product.
Read about it [here](http://www.blackhat.com/docs/asia-16/materials/asia-16-Sivakorn-Im-Not-a-Human-Breaking-the-Google-reCAPTCHA-wp.pdf). 

