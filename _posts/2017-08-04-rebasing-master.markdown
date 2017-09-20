---
layout: post
title:  "Rebasing with master on Git"
date:   2017-08-04 01:57:45 -0700
---

## No conflicts

Lets call your branch `dev`.

`git checkout dev` to go to your branch.

`git fetch` to fetch the updates from master.

`git rebase origin master` to replay your changes on top of what other people have done and 
committed to master.

## With conflicts

After running the last command, you will get an error message saying you can't merge.
Fix ALL the conflicts on the files that git complained about,
and do `git add <path-to-file-with-conflict>` on each file that had conflicts 
(that you just fixed).

Once you have fixed ALL the conflicts in the code base, now you can do
`git commit -m 'Fixed merge conflict'`.
Do not commit before fixing everything.
Afterwards, you should get a message saying that all conflicts are resolved.

And now do `git push origin dev` to get your updated branch reviewed and merged. 

## Pitfalls

Given a workflow that looks like this:
```
         E --- F --- G --- H --- I --- J --- K --- L --- M --- N --- P (branchA)
        /                 /
       /                 /    
master ---------------- D 
       \               /
        \             /
         A --- B --- C  (branchB)
```
If the merge conflict occured at point D due to branchB's merged changes,
and you later want to rebase branchA with master,
you'll have to merge the conflicts for ALL the comments until the divergence point D
in branchA.

This means you may have a never ending round of rebasing commits
if you made lots of new changes since the divergence point.

Its ok to commit often, so the workarounds are:

1. If there are not too many conflicts: update the conflicts in branchA manually.
	This is easiest to do. 
2. Squash all the commits in branchA, then you only need to rebase once. 
















