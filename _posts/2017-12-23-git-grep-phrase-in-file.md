---
layout: post
title:  "Git grep <phrase> **/<filename>"
date:   2017-12-23
---

To search for `phrase` inside a large, complicate git repository with lots of files
with the same name, do 
```
git grep <phrase> **/<filename>
```

This will output a list of files called `filename` within a folder 
in the main repository, with `phrase` inside the files.

For example, given a directory like this:
```
-- top_level
  -- folder_alice
     view.py // contains "user"
     model.py
  -- folder_bob
     view.py // does NOT contains "user"
     model.py
  -- folder_charlie
     view.py // contains "user"
     model.py
     -- folder_inner
        view.py // contains "user"
        test.py
```

then `git grep user **/view.py` will output the files
`folder_alice/view.py` and `folder_charlie/view.py`
that contain the word `user`.



