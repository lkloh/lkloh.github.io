---
type: post
title: "Version dependency conflict"
date: 2018-04-16
---

Sometimes libraries you install on a machine may depend on an older version for some reason or another.
So here is how you downgrade to an older version:

```
apt-cache search desired_package_to_install*
```

Find the exact version you want.
Suppose its `desired_package_to_install1.0.0=1.0.2g-1ubuntu4.1`.

Now get rid of the newer installed version
```
sudo apt-get uninstall desired_package_to_install
```

And install the older version:
```
sudo apt-get install desired_package_to_install1.0.0=1.0.2g-1ubuntu4.1
```

Make sure future updates do not overwrite the older version:
```
sudo apt-mark hold desired_package_to_install
```

Thanks [Stack Overflow](https://askubuntu.com/questions/630439/libssl-dev-version-dependency-conflict-with-installed-libssl1-0-0/892032)!
