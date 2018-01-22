---
type: post
title: "What formal methods can and cannot do for AWS"
date: 2018-01-01
---

Summarized from [here](http://lamport.azurewebsites.net/tla/formal-methods-amazon.pdf).

## What it does

* Get the design right - there is no hope of having the correct code without
  the correct design
* Improve understanding of the design for engineers -
  having a clearer mental model helps them work more accurately
* Help engineers write code with better test cases 
  that assert that the invariants hold

## What it cannot do

* Verify that the code implements the design specification in TLA+ correctly
* Generate code from the design - the systems AWS builds are too complex for that

## Next steps

* Use the TLC model checker to find edge cases in the design,
  and use those edge cases to write more unit tests in the code.

## Conclusion

Formal methods are useful for writing designs in complex industrial
scale systems. However, what would really help is being able to 
generate actually executable code form the design specifications,
but that is unlikely to happen in practice anytime soon.


