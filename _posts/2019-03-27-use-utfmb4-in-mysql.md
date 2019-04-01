---
type: post
title: "Use utfmb4 instead of utf8 in MySQL"
date: 2019-03-27
---

MySQL's UTF8's encoding only supports 3 bytes per character,
but the real UTF8 encoding supports up to 4 bytes per character.
MySQL did not fix the encoding problem in UTF8, but instead
fixed it in a new character set called UTF8MB4.
According to [this post](https://medium.com/@adamhooper/in-mysql-never-use-utf8-use-utf8mb4-11761243e434),
they did not advertise the bug in UTF8 and urge
users to convert to UTF8MB4 to avoid negative publicity.


