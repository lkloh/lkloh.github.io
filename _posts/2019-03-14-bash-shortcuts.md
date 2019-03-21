---
type: post
title: "Bash shortcuts"
date: 2019-03-14
---



## Making a series of parent directories

Assuming directories "a" and "b" don't exist,
```
mkdir a/b/c
```

will return this error
```
mkdir: a/b: No such file or directory
```

To make directories "a/b/c", use

```
mkdir -p a/b/c
```
to create all the directories on the three levels.

## Finding files with a particular name

```
find <folder-name>/ -name "<search-term>"
```

So given a folder called "vacation-pictures",
if you want to search for all images taken in "greece", dp
```
find vacation-pictures/ -name "*greece*"
```

To do a case-insensitive search:
```
find vacation-pictures/ -iname "*greece*"
```

To delete all vacation pictures with "greece" as part of their name:
```
find vacation-pictures/ -iname "*greece*" -delete
```

To run an arbitrary function on selected files:
```
find vacation-pictures/ -iname "*huge*" -exec compressionTool {} \;
```

To learn more, see `man find`.

## git grep

I usually do
```
git grep "moment.date"
```
to look for something in an entire directory.

To make things easier to read:
```
git --color grep "moment.date"
```

To add line number
```
git --color -n grep "moment.date"
```

Grep has a lot of flags, so `man grep` to get all possibilities.

## Making a request to a website with CURL

Modified from [here](https://egghead.io/lessons/http-make-http-requests-in-bash-with-curl).

Making a GET request from the Star Wars API:
```
curl https://swapi.co/api/people/2
```

Making a POST request:
```
curl -X POST -H "Content-Type: application/json" -d "{"title: "hello", "author": "world"}" http://example.com
```

Outputting the response to a file
```
curl -iL https://google.com -o gresponse.txt
```

Piping formatted json responses to make it easier to read
```
curl https://swapi.co/api/people/1 | jsome
```
[jsome](https://www.npmjs.com/package/jsome) helps format JSON responses, you need it installed first.

## Creating multiple files

```
mkdir -p package/{p1,p2,p3}/src
```
creates a parent directory `package` with three children `p1`, `p2`, `p3`,
and each `px` has a `src` folder inside.

and 
```
touch test-{1..10}
```
creates these files
```
test-1  test-10 test-2  test-3  test-4  test-5  test-6  test-7  test-8  test-9
```

Similarly, 
```
touch letters-{a..z}
```
creates these files:
```
letters-a	letters-g	letters-m	letters-s	letters-y
letters-b	letters-h	letters-n	letters-t	letters-z
letters-c	letters-i	letters-o	letters-u
letters-d	letters-j	letters-p	letters-v
letters-e	letters-k	letters-q	letters-w
letters-f	letters-l	letters-r	letters-x
```


