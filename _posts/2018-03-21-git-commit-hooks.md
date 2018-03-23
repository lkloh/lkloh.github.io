---
type: post
title: "Git hooks"
date: 2018-03-21
---

If you want to run something automatically before you commit on git 
(such as a linter), 
you want to use [Git hooks](https://git-scm.com/book/en/v2/Customizing-Git-Git-Hooks).

Inside any git repository, look inside
```
<git-repo>/.git/hooks
```

to find a directory of git hooks for you to configure.
There are sample files with the work `<file>.sample` at the end,
so change the name to `<file>`, removing `.sample`
to customize what you want to do.

For example, I changed my `<git-repo>/.git/hooks/pre-commit.sample` file name
to `<git-repo>/.git/hooks/pre-commit` and added the line
```
echo "hello world"
```

and each time after I run `git commit -m "I made a commit"`,
my terminal outputs "hello world" now.


