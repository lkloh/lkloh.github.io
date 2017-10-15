---
layout: post
title:  "Process vs Thread"
date:   2017-10-13
---

[Memory space they run in.](https://stackoverflow.com/questions/200469/what-is-the-difference-between-a-process-and-a-thread)

## Thread

* Threads (in the same proces) run in a shared memory space

## Process

* Processes run in separate memory spaces
* Executes a program

```
 -----------------------
|        Process        |
|   -----------------   |
|  |   Thread        |  |
|   -----------------   |
|   -----------------   |
|  |   Thread        |  |
|   -----------------   |
|   -----------------   |
|  |   Thread        |  |
|   -----------------   |
|   -----------------   |
|  |   Thread        |  |
|   -----------------   |
|                       |
 -----------------------

  -----------------------
|        Process        |
|   -----------------   |
|  |   Thread        |  |
|   -----------------   |
|   -----------------   |
|  |   Thread        |  |
|   -----------------   |
|   -----------------   |
|  |   Thread        |  |
|   -----------------   |
|   -----------------   |
|  |   Thread        |  |
|   -----------------   |
|                       |
 -----------------------

 -----------------------
|        Process        |
|   -----------------   |
|  |   Thread        |  |
|   -----------------   |
|   -----------------   |
|  |   Thread        |  |
|   -----------------   |
|   -----------------   |
|  |   Thread        |  |
|   -----------------   |
|   -----------------   |
|  |   Thread        |  |
|   -----------------   |
|                       |
 -----------------------
```





















