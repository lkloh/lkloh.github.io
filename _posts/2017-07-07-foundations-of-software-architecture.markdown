---
layout: post
title:  "Foundations for the study of Software Architecture"
date:   2017-07-07
---

Find the original 1992 paper [here](https://dl.acm.org/citation.cfm?id=141884).
This is a summary of key points

## Software architectural components

1. Elements - data / processing elements
2. Form - relationships among elements
3. Rationale - System requirements

## Software design

* Design is separate from implementation
* Design has its own unique tools/notations

## 	Programming-in-the-large

* Integrates software design + implementation
* Implementation language is a superset of software design notations

## Software architecture (vs sofware design)

* Has set standards
* Needs formal training 

## Software architecture

* # design elements: many
* Scaling: add more distinct design elements
* Configurations: pipelined processing; multi-processor systems


## Hardware architecture 

* # design elements:  few
* Scaling: replicate the design elements
* Configurations: pipelined machines; multi-processor machines

## Building architecture

* Multiple views needed to categorize all aspects
* Styles are importent
* Engineering principles are needed

## Why software is expensive

* Evolution - systems evolve and are adapted to new uses
* Customization - no standard templates to use

## How to decrease the cost of software

* Separate "must-haves" from "nice-to-haves"
* Describe different parts of the architecture with the appropriate view
* Determine interdependencies between different components of the system

## Modeling Software architecture

### Elements 

* processing
* data
* connecting

### Form

* properties - constraints elements
* relationships - constraing how elements interact

### Rationale

Why were various design choices made?

## What is architectural Style?

Architecture: formal arrangement of elements

Architectural Style: Abstracts elements from various specific architectures.

Less constrained than architecture

## Multi-phase Architectural Style - Compiler

1. Lexical analysis - characters => tokens
2. Syntactic analysis - tokens => phrases
3. Semantic analysis - phrases => correlated phrases
4. Optimization (optional) - correlated phrases => annotations as hints
5. Code deneration - annotations => object code

### Elements

Processing
* lexer
* parser
* semantor
* optimizer
* code generator

Data
* Chracters
* Tokens
* Phrases
* Correlate phrases
* Annotated Phrases
* Object code

Connecting
* N/A

### Form

* Preferred elements - optimizer + annotated phrases
* Linear relationship: tokens - sequence of characters
* Linear relationship: phrases - sequence of tokens
* Nonlinear: phases & correlated phrases
* Tokens and characters have an order that must be preserved

### Rationale

Source code => object code

## Benefits of software architecture

* Software architecture: _Framework to satisfy system requirements_
* Clear documentation
* Automated analysis - consistency with system requirements 
* Describe expected problems
* Reuse previous work - easier to reuse when there are less constraints
* Understand important properties/relationships for systems








































