---
layout: post
title:  "Transpiler or Compiler?"
date:   2017-10-24
---

Babel's official website states that 
```
BABEL IS A JAVASCRIPT COMPILER.
User next generation JavaScript, today.
```

Really, it just does this:
```
Code written in ES6/ES7 === Babel ===> Code written in ES5
```

So not as epic as this:
```
C++ === C++ Compiler ===> Assembly language (Most dev's can't read it)
```

Disclaimer: My dad can read assembly language.
When he was learning about computer science, 
some older students still programmed on punch cards.
The worst programming mistakes happened when 
they were carrying their program their program made of punch cards
to the shared machine for compilation,
and they dropped the box on the long walk to there.

Most people can't read the end result of this either
```
Java === Java Compiler ===> Bytecode
```

But ES5 is perfectly readable to most people who are capable of written
a program in ES6. 

## Official definitions

Compiler: translates a program from one language to another.
Since Babel translates a program from ES6 to ES5, it is therefore a compiler.

I could also compile Chinese to English then.
Not too sure about the reverse though, output may be buggy.

## Social definition

* Compiler: translates a program from a high level language (e.g. Python)
	to a low level language (e.g. Assembly language)
* Transpiler: translates a program from a high level language (e.g. Fortran)
	to another high level language (e.g. C++).



