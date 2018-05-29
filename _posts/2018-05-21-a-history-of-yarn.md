---
type: post
title: "A history of Yarn"
date: 2018-05-21
---

Summarized from [here](https://code.facebook.com/posts/1840075619545360).

## What is Yarn?

Package manager for JavaScript.

## Why develop Yarn when NPM (the most popular package manager) already exists?

NPM was used at Facebook for years, but they started getting issues with
consistency, security, and performance as their codebase and engineers grew.

Yarn was developed to be a fast, reliable, ad secure alternative package manager for JavaScript.

## What does Yarn let you do?

Install packages in the NPM registry more quickly,
manage dependencies consistenly across machines/ in secure offline environments.

## How JavaScript package management evolved

* Before package managers: Rely on a few dependencies stored 
directly in projects, or served by a CDN.
* NPM (first major JavaScript package manager): Build after Node.js was developed, became very popular
* Facebook depended on NPM initially, but had problems with consistency when installing dependencies across
  different machines and users, time taken to load dependncies,
  and security concerns about dependencies.
* Initially Facebook engineers commited package.json and manually ran `npm install`,
  which didn't work for CI environments that had to be cut off from the
  internet for security and reliability purposes.
* Then they checked all of the `node_modules` into their repository,
  but it made upgrading packages very difficult.
  Merging a minor upgrade could take an entire day.
* Then they ziped the `node_modules` folder and uploaded it to an internal CDN so 
  engineers and the CI could download and extract the files consistently.
  They also needed to do extra work to ensure dependency versions were always in sync.

## Building Yarn to address the core issues around NPM

* Facebook figured out that other engineers across the industry had similar issues 
  and solutions to NPM as they scaled, and decided to collaborate with Exponent,
  Google, and Tilde to build a solution for everyone.
* Yarn is tested on every major JS framework, and use cases across several major
  software companies.


## How nondeterminism in NPM causes inconsistencies

* In Node, dependencies are placed in the `node_modules` directory in the project.
  The `node_modules` file structure can differ from the real dependency tree 
  if several modules have different versions of the same dependency.
* NPM installs dependencies into `node_modules` based on the order in which dependencies
  are isntalled, so the structure of the directory may very between people,
  depending on what they already have install.

## How Yarn uses determinism to ensure consistency

* Yarn uses lockfiles and a deterministic algorithm to lock down installed
  dependencies to a specific version and ensure every install results in the same file structure
  for `node_modules` on any machine.

Installation
1. Resolving dependencies: Recursively look up each dependency
2. Fetching dependencies that are not in a global cache directory.
3. Copy files needed from the global cache to the local `node_modules` directory













