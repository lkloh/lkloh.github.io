---
layout: post
title:  "Commit the yarn.lock file"
date:   2017-07-06
---

Yarn is a package manager.
It records all the package dependencies for a project
you're developing to ensure consistency for someone else
checks out what you've done.
This helps avoid the 'works on my machine' problem.

Yarn needs to know which version you developed on
to make sure that package dependencies are installed
in the correct place and order on a machine,
to avoid having installation issues with dependencies.

The yarn.lock file is automatically generated
and tracks the version number of each dependency.
It may be updated if you upgraded a package locally
or added a new dependency.
In that case, it should be committed to the repo.

## Edit, Feb 2018

But don't commit the yarn.lock file if you're working on a shared repo 
and it changed without you updating a dependency.
It's probably a problem with your local environment that became out of sync
with the master version. 
