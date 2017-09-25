---
layout: post
title:  "Sauce Labs"
date:   2017-07-20 04:42:23 -0700
---

[Sauce Labs](https://www.ministryoftesting.com/2013/06/a-look-inside-saucelabs/)
allows automated tests to be run in the cloud.
In particular, they allow for the tests to be run in
many combinations of OS/browser.
If you've ever had to test a webapp on just Chrome and Firefox, 
you'll know just how valuable this is.
They do that by running users' tests on their VMs. 

## Latency over a network

Sometime SauceLabs users write tests with local dependencies,
which can cause issues with "works on my laptop, not in the cloud".
For example, if someone wrote such a test:
```py
from datetime import datetime
import time

def test_waited_5_seconds():
	timenow = datetime.now()
	time.sleep(5)
	timelater = datetime.now()
	assert (timelater - timenow).total_seconds() == 5
```

Doing stuff over a network like the internet has
all sorts of latency issues to consider.
Its possible that `timelater - timenow` is more than 5 seconds
when run in the cloud.

## Solving the latency problem

According to [Sauce Labs](https://saucelabs.com/blog/how-to-lose-races-and-win-at-selenium),
many Selenium tests fail because websites are designed to be used by a human being,
who needs time to respond to anything that happens.
Selenium can respond to changes much faster than any human can.
Since many websites use lazy loading (loading on demand),
Selenium sometimes tries to interact with page elements that have not been loaded yet.

So when testing with Selenium,
it is a good idea to `assert` that an element is loaded,
before asserting something else,
For example, make sure the `submit` button on a form is loaded,
before clicking on it to verify
that it takes you to the `confirm sign up for mailing list` page.

The way to verify the element is loaded
is to try a few times to check that it is loaded, before failing. 
Something like
```js
def test_submit_form(self):
	submit_button = self.spin_assert('#submit_credentials')
	submit_button.click()
	url = driver.getCurrentUrl(self.driver);
	assert urlparse.urlparse(url) == '/successful_submit.html'

def spin_assert(self, css_selector):
	for _ in range(3):
		try:
			return self.driver.find_element_by_css_selector(css_selector)
		except NoSuchElementException:
			sleep(1)
	raise 'Element with selector not found' % css_selector
```












