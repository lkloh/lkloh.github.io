---
type: post
title: "A function to check passwords that fails when run with optimizations"
date: 2017-12-27
---

The package is written in Python, and used an `assert` statement to check whether the password
entered by the user the correct passwords as the one stored on the system.
Obviously, if the user trying to log in enters a different password,
the function is supposed to raise an exception.

But running it with optimizations enables (e.g. 0 or 00 flags)
will not call any `assert` statements, so the function will never throw an exception.

Read more [here](https://github.com/rohe/pysaml2/issues/451).

I thought that stored the plaintext of the password, instead of the hash,
was also a security issue [though](https://github.com/rohe/pysaml2/commit/efe27e2f40bf1c35d847f935ba74b4b86aa90fb5).

