---
layout: post
title:  "Python Test Suites"
date:   2017-10-05
---

How to run the same tests bundled in a class under different environments:

```py
import random
import math
import unittest
from unittest.mock import patch

class TestPatchClass(unittest.TestCase):

    def test_one(self):
        print(random.random())

    def test_two(self):
        print(random.random())

    def test_three(self):
        print(random.random())
```

Run the suite under a patch, 
```py
if __name__ == '__main__':
    # unittest.TextTestRunner().run(unittest.makeSuite(TestPatchClass))

    with patch.object(random, 'random') as mock_random:
        mock_random.return_value = 0.5
        unittest.TextTestRunner().run(unittest.makeSuite(TestPatchClass))

    with patch.object(random, 'random') as mock_random:
        mock_random.return_value = 0.7
        unittest.TextTestRunner().run(unittest.makeSuite(TestPatchClass))
```
