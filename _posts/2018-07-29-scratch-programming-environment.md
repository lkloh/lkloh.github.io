---
type: post
title: "Scratch programming environment"
date: 2018-07-29
---

Summarized from [here](http://web.media.mit.edu/~jmaloney/papers/ScratchLangAndEnvironment.pdf).

The main motivation for developing [Scratch](https://scratch.mit.edu/) was to encourage
young people to by experimenting in an environment they found fun, and to collaborate with their peers.
The original authors made Scratch to teach at young people programming.
Ideally, they are between the age of 8-16, regularly spend time at after-school computer centers,
and are motivated to tinker with Scratch for fun and learn from their peers without
and explicit instruction.
Though, Scratch eventually got picked up by schools as well.

Since the point of Scratch is to "learn by tinkering",
the Scratch interface was designed to make scripting simple,
and execution and data visible.

The single-window, multi-pane UI ensures key components are always visible,
instead of showing palettes on demand which could might cause trouble with discoverability.
There are only eight categories of commands
(e.g. motion, looks, sound, control) that can be viewed without scrolling,
to avoid overwhelming the user.

Scratch is always live (not edit/run mode),
so users can click on a command at any tiem to see what it does,
to eliminate context switching between edit and compile modes.

To provide visual feedback on script execution,
when a script is running, it is surrounded by a glowing white border 
to help the user understand when scripts are triggered and how long they run for.
Errors (e.g. zero division) are cause the border of the script
and the block causing the error to turn red.
Control flow can be seen by enabling single-stepping from the menu,
causing blocks to flash as they run.

There are no error messages in Scratch by making blocks failsoft -
they do something "sensible" when presented with faulty inputs. 
Obviously this does not eliminate errors, only make a faulty program
feel more correct than one showing errors all over the place.

Variables in Scratch are turned into concrete objects the user can manipulate 
to make the easier to understand and tinker with.

Command sets are intentionally minimized to avoid dominating the limited screen space.









