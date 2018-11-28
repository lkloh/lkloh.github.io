---
type: post
title: "Changing your bash setup"
date: 2018-11-27
---

Your command line on linux typically shows
```
$
```
by default.

To change things, you can modify the `PS<X>` variables.

Setting `PS1="yolo"` in your `.bashrc` file and sourcing it will turn your
command prompt into
```
yolo
```

Read more [here](https://www.cyberciti.biz/tips/howto-linux-unix-bash-shell-setup-prompt.html).

## Git

To show the branch you're on in Git, you can do `PS1="branch $(__git_ps1) >"`,
which will turn your command line into

```
branch (master) >
```

for example when on the master branch in a git repository.

Read more [here](https://blog.backslasher.net/git-prompt-variables.html).






