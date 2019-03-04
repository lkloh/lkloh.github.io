---
type: post
title: "Making kubectl log continuously"
date: 2019-02-21
---

Modified from [here](https://stackoverflow.com/questions/39454962/kubectl-logs-continuously).

I was trying to understand a bug and get continuously logging
while I was playing with the webapp to reproduce the bug.

```
kubectl logs --help
```

and then
```
kubectl logs -f <pod-id>
```

did the trick.



