---
type: post
title: "Render first, then update"
date: 2018-08-26
---

What do you do if you have a dropdown list to populate,
that requires you to make a request to a server that may take a little while
to return with the required data to populate the dropdown list?

There are two obvious choices:
1. Wait for the request to return with the data,
  then render the dropdown list.
  This means making a callback in the request for data to render the dropdown list _after_ the data
  has been successfully retrieved.
2. Render the dropdown list first, then update it after you have all the data.
  This means render the empty dropdown list first,
  then inside the callback, update the dropdown list with all the options.

No. 2 is usually the better choise just because you don't keep the user waiting for so long
before rendering. People have short attention spans.


