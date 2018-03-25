---
type: post
title: "Installing Pandas"
date: 2018-03-23
---

I was trying to install [Pandas](https://pandas.pydata.org/),
and this worked:

```
sudo pip install pandas
```

when I ran
```
python
```

to open the interpreter and did

```
import pandas
```

However, opening the interpreter by typing
```
python3
```

and then

```
import pandas
```

gave this error:
```
ImportError: No module named 'pandas'
```

To fix this,

```
pip3 install pandas
```
worked, or else

```
python3 -m pip install pandas
```

Thanks [Stack Overflow](https://stackoverflow.com/questions/25172981/pandas-and-python3-4-co-existing-with-python-2-7)!










