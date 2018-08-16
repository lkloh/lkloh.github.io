---
type: post
title: "Kill all running processes"
date: 2018-08-14
---

When figuring out which processes to kill by doing
```
ps aux | grep <process>
```
is going to take too long due to the number of running processes, try
```
killall5 -9
```
to kill all running processes except the login shell and a couple others.

Thanks [Stack Overflow](https://superuser.com/questions/161531/how-to-kill-all-processes-in-linux)!

