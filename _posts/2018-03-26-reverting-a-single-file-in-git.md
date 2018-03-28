---
type: post
title: "Reverting a single file after committing several files"
date: "2018-03-26"
---

Some somethings I make a pull request that changes files `a.py`, `b.js`, and `c.json`.
I want the changes I made to `a.py` and `b.js`, but I want to discard the changes in `c.json` 
as I accidentally committed that file.

To undo the changes made to just `c.json`, but keep my changes to `a.py` and `b.js`, use 
```
git log
```

to find the last commit to revert `c.json` to.

Then do 
```
git checkout <last-commit-to-revert-file-c-to> path/to/c.json`
```

Finally, commit file `c.json` again, and all is well.

Thanks [Stack Overflow](https://stackoverflow.com/questions/2733873/reverting-a-single-file-to-a-previous-version-in-git).


