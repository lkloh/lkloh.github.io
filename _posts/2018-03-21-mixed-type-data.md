---
type: post
title: "Mixed type data"
date: 2018-03-21
---

Sometimes data you collect may not be in the same type.
This is especially true if it comes from many sources.
It leads to inconsistencies when you filter things, for example:

```js
var mixed_type = {
    three: 3,
      three_str: '3',
        four: 4,
          four_str: '4',
            five: 5,
};

function loose_filter_for_three(dict) {
    var num_values_equal_to_three = 0;
      for (key in dict) {
            if (dict[key] == 3) {
                    num_values_equal_to_three += 1;
                        }
                          }
                            return num_values_equal_to_three;
}


function strict_filter_for_three(dict) {
    var num_values_equal_to_three = 0;
      for (key in dict) {
            if (dict[key] === 3) {
                    num_values_equal_to_three += 1;
                        }
                          }
                            return num_values_equal_to_three;
}

console.log(`Loose filter: num values equal to three ${loose_filter_for_three(mixed_type)}`);
console.log(`Strict filter: num values equal to three ${strict_filter_for_three(mixed_type)}`);
```
