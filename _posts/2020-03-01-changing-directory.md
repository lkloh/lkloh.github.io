---
type: post
date: 2020-03-01
title: "Changing Directory"
---

I wanted to run a script in order to remove the `bar` directory in the folders `./foobar/dir_1` and `./foobar/dir_2`.

```
#!/usr/bin/env bash

foo() {
  cd $1
  rm -r bar
}

foo ./foobar/dir_1
foo ./foorbar/dir_2
```

But there is a problem with this script that uses relative paths. The first statement `foo ./foobar/dir_1` behaves as expected, but the second statement `foo ./foorbar/dir_2` fails as the first statement changes the directory. 

In order to circumvent this, I first tried doing this:
```
#!/usr/bin/env bash

foo() {
  cd $1
  rm -r bar
}

CURRENT_DIR=pwd
foo ./foobar/dir_1

cd $CURRENT_DIR
foo ./foorbar/dir_2
```
which did the trick.

However, someone pointer out to me that using `pushd` and `popd` would be even better and cleaner and I could just [return to the original directory](https://opensource.com/article/19/8/navigating-bash-shell-pushd-popd) after the command was executed.
```
#!/usr/bin/env bash

foo() {
  pushd $1
  rm -r bar
  popd
}

foo ./foobar/dir_1
foo ./foorbar/dir_2
```
