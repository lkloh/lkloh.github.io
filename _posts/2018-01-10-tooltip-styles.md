---
layout: post
title:  "What happened when I added a tooltip to a disabled button"
date:   2018-01-10
---

The styles for the tooltip comes out differently in these cases!

```js
// tooltip has black background, white text
<div class="button-container" disabled="true">
    <button>button</button>
    <custom-tooltip style="background:black;color:white;">Tooltip with weird styles</custom-tooltip>
</div>
```

versus

```js
// tooltip has gray background, white text
<button disabled="true">
    button
    <custom-tooltip style="background:black;color:white;">
        Tooltip with weird styles
    </custom-tooltip>
</button>
```

You want to put the button and its tooltip as children inside a containing div,
instead of making the tooltip a child of the button.

