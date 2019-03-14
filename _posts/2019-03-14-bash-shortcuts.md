---
type: post
title: "Bash shortcuts"
date: 2019-03-14
---

## Making a series of parent directories

Assuming directories "a" and "b" don't exist,
```
mkdir a/b/c
```

will return this error
```
mkdir: a/b: No such file or directory
```

To make directories "a/b/c", use

```
mkdir -p a/b/c
```
to create all the directories on the three levels.

