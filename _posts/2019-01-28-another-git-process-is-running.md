---
type: post
title: "Another git process is running in the repository"
date: 2019-01-28
---

If you get such a warning on running a git command:
```
Another git process seems to be running in this repository, e.g.
an editor opened by 'git commit'. Please make sure all processes
are terminated then try again. If it still fails, a git process
may have crashed in this repository earlier:
remove the file manually to continue.
```

delete the `.git/index.lock` file in your repository by doing
```
rm -f .git/index.lock
```

This happened to me when I was running VSCode to edit files,
which as a git terminal inbuilt that is very slow,
and I also had iTerm open to run git commands more quickly.

Thanks [Stack Overflow](https://stackoverflow.com/questions/38004148/another-git-process-seems-to-be-running-in-this-repository).

