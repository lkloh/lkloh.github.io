---
type: post
title: "Jade a href"
date: 2018-02-07
---

I was trying to add a web link in a jade template

```
a(href='https://www.google.com') Link to Google
```
would technically do it, but I kept getting an error until I tried
```
a(attrs={href: `https://www.google.com`}) Link to Google
```

