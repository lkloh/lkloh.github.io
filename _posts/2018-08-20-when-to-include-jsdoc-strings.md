---
type: post
title: "When to include JSDoc strings"
date: 2018-08-20
---

If you are passing a configuration dictionary to a constructor,
and there are many potential configurations,
it may be advisable to write a JSDoc explaining what the configurations are.

For example:
```js
function Animal(config) {
  this.config = config;
}

const animal = new Animal({
  domain: 'eukaryota',
  kingdom: 'animalia',
  phylum: 'chordata',
  class: 'mammalia',
  order: 'primates',
  common_name: 'monkey',
  num_legs: 4,
});
```

could be made more clear by explaining the possible
configuration parameters in the docstring like this:

```js
/**
 * Initializes an animal object
 * @constructor
 * @param config - dictionary of parameters describing an animal
 * @param config.domain {string}
 * @param config.kingdom {string}
 * @param config.phylum {string}
 * @param config.class {string}
 * @param config.order {string}
 * @param config.common_name {string} - name the animal is most commonly known by
 * @param config.num_legs {number} - number of legs the animal has
 */
function Animal(config) {
  this.config = config;
}

const animal = new Animal({
  domain: 'eukaryota',
  kingdom: 'animalia',
  phylum: 'chordata',
  class: 'mammalia',
  order: 'primates',
  common_name: 'monkey',
  num_legs: 4,
});
```
