---
type: post
title: "expect({sth}, 'message').to.equal({sth})"
date: 2018-03-09
---

To output an error message when something goes wrong in a JavaScript test,
instead of printing
```js
expect(<expected-value>).to.equal(<expected-value>);
```

do

```js
expect(<expected-value>, "error messsage if something goes wrong").to.equal(<expected-value>);
```

instead.


