---
type: post
title: "OpenGL Deprecation"
date: 2018-06-12
---

[Apple deprecated support got OpenGL and OpenCL with the release of macOS 10.14](https://www.pcgamer.com/developers-fear-for-mac-gaming-as-apple-deprecates-opengl-support/) in 2014.
Which happens to be a cross-platform API for 3D graphics.

Instead, they told everyone to use [Metal](https://developer.apple.com/metal/),
their proprietary 3D graphics API.

Meaning games and graphics using OpenGL need to use Metal instead,
and apps using OpenCL need to use Metal/ Metal performance Shaders.
And Metal isn't cross-platform, so developing games on Windows 
and supporting it on MacOS isn't going to be as straightforward going forward.
It used to be "Use OpenGL to make a cross-platform game".
Now you'll have to spend hours porting it to Mac if you developed a game in OpenGL on Windows.

