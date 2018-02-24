---
type: post
title: "Triggering JQuery events"
date: 2018-02-23
---

One can force a JQuery event to be triggered on a DOM element by using 
[trigger](https://stackoverflow.com/questions/10547622/trigger-change-event-select-using-jquery).

Example here:
```
<!DOCTYPE html>
<html>
<head>
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js"></script>
  <script>
    $(document).ready(function() {
      $('.btn').click(function(e, params) {
        console.error('hello');
        console.error(params);
      });
      $('.btn').trigger('click', ['lkloh']);
    });
  </script>
</head>

<body>
  <button class='btn'> Press me </button>
</body>
</html>
```


