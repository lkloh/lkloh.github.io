---
layout: post
title:  "keyCode vs which"
date:   2017-12-01
---

When listening for a keypress event in JavaScript,
better to use `which` in jQuery, as it is standardized across browsers.

Some browsers use `which` in JavaScript, others use `keyCode`.
Hard to detect sometimes if you only develop on Chrome.


