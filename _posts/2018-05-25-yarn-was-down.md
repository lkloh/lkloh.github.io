---
type: post
title: "Yarn is down"
date: 2018-05-25
---

Yarn was down, so doing
```
yarn install
```

kept failing for about an hour.
Must have been due to it being 4pm before a long holiday weekend,
and some people were trying to get a deploy in before the long break.
Not sure whether its a good or bad thing,
as many people using yarn may already be on leave,
but as a downside it violates the "never deploy on Fridays" rule.

Issue was caused by the fact that Yarn uses NPM.
NPM [was migrating their repository to use CloudFlare](https://news.ycombinator.com/item?id=17158840).
As Yarn used CloudFlare already,
and had a CNAME from Yarn to NPM,
and CloudFlare had a security restriction that one CloudFlare account 
cannot have DNS records pointing to another CloudFlare account,
NPM's migration broke Yarn's CNAME to NPM's registry.
Thus Yarn went down.
In particular, the registry [https://registry.yarnpkg.com](https://registry.yarnpkg.com) went down,
but the NPM registry [https://registry.npmjs.com](https://registry.npmjs.com) was fine.

A workaround during the outage proposed by [@fathyb](https://github.com/yarnpkg/yarn/issues/5885)
was:
```
yarn config set registry "https://registry.npmjs.org"
yarn install --no-lockfile
```




