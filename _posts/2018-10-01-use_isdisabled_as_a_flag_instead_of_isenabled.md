---
type: post
title: "Use isdisabled as a flag instead of isenabled"
date: 2018-10-01
---

Given this function to update a user's address
```js
function update_user_address(user_id, new_address) {
  let user = this.user.get(`user_id`);
  user.set(`address`, new_address`);
  this.user.set(`user_id`, user);
}
```

supposed you wanted to check whether the user is an active user or not,
before bothering to update their address for performance optimization reasons.

What should you do?

```js
// option A
let current_user_id;

class User(options) {
  current_user_id++;
  this.user_id = current_user_id;
  this.name = options.name;
  this.phone = options.phone;
  this.address = options.address;
  this.is_active = !!options.is_active;
}

function update_user_address(user_id, new_address) {
  let user = this.user.get(`user_id`);
  if (user.is_active) {
    user.set(`address`, new_address`);
    this.user.set(`user_id`, user);
  }
}
```

or 


```js
// option B
let current_user_id;

class User(options) {
  current_user_id++;
  this.user_id = current_user_id;
  this.name = options.name;
  this.phone = options.phone;
  this.address = options.address;
  this.is_disabled = !!options.is_disabled;
}

function update_user_address(user_id, new_address) {
  let user = this.user.get(`user_id`);
  if (!user.is_disabled) {
    user.set(`address`, new_address`);
    this.user.set(`user_id`, user);
  }
}
```

You _should_ use option B by default, so that if someone forgot to set the flag for
`is_disabled`, then it would be `undefined` by default.
And `!!undefined` would be `false`, so the user would _not_ disabled by default.
thus the check for `!user.is_disabled` would return `true`, and thus
we would update the user's address by default and err on the side of keeping the information fresh.

Not if you had used `is_enabled` by default,
and then someone forgot to set the flag for `is_enabled`, 
we would have `!!is_enabled` return `false,
so the user is _not_ enabled by default,
so we would err on the side of letting updates be disregarded, which is generally a bad practice.



