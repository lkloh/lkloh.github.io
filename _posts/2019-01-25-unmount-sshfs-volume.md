---
type: post
title: "Unmounting an SSHFS volume"
date: 2019-01-25
---

If an SSHFS volume needs to be unmounted, try 
[this](https://github.com/osxfuse/osxfuse/issues/45#issuecomment-21943107):

Get the sshfs process
```
pgrep -lf sshfs
```
and record it's `pid`.

Kill the process
```
kill -9 <pid_of_sshfs_process>
```

and then force unmount the directory
```
sudo umount -f <sshfs_directory>
```

