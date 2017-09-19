---
layout: post
title:  "Killing Ports"
date:   2017-08-05 01:57:45 -0700
---

Or when you get an `EADDRINUSE` 
because you didn't shut down your server properly,
to find out what the processes still running on that port are, do

`lsof -i :<port-num>`.

This will print all of the processes and their PIDs, so you can do

`kill PID` to kill a particular process.

If there are lots of processes on that port and you want to kill them all, do

`kill $(lsof -t -i:<port-num>)`.

Thanks [Stack](https://stackoverflow.com/questions/11583562/how-to-kill-a-process-running-on-particular-port-in-linux) 
[Overflow](https://stackoverflow.com/questions/3855127/find-and-kill-process-locking-port-3000-on-mac)!