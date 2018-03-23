---
type: post
title: "Webpack watch"
date: 2018-03-20
---

Summarized from [here](https://webpack.js.org/configuration/watch).

Webpack watches files and recompiles them when they change.
Thus allowing you to making changes to the source code and then
see them update after refreshing the page, instead of building everything from scratch again.
The update is seen after page refresh is made as the source code gets compiled every time the change is saved,
so the page refresh merely shows the latest compiled output.

## watch

```
watch: true
```

to turn on watch mode to watch for changes in the files. 
Off by default to avoid too much CPU  utilization, presumably.

## watchOptions

```
watchOptions: {
  aggregateTimeout: 300, // delay before compiling after a change (millisecond)
  ignored: /node_modles/ // exclude a huge folder was watching many files increases CPU utilization
  poll: 1000, // how often to check for changes (millisecond)
}
```

