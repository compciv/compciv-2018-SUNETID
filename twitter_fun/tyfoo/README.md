# Fun with the Twitter API

This repo contains some kludgy scripts as a rough way of showing how programming and APIs go together.

## Context

Some background reading:

- [Exploring the basics of the Twitter API with Twython](http://2017.compciv.org/guide/topics/python-nonstandard-libraries/twython-guide/twitter-twython-api-basics.html)
- [Getting Started with Tweepy](http://www.compjour.org/tutorials/getting-started-with-tweepy/)
- [A Peak of Grammar Correction with Twython](http://2017.compciv.org/guide/topics/python-nonstandard-libraries/twython-guide/twitter-twython-simple-grammar-corrector.html)

note: the above examples talk about using the [Twython](https://github.com/ryanmcgrath/twython) library, whereas the code examples here use [Tweepy](http://tweepy.readthedocs.io/). The libraries have different design sensibilities but the main concepts are the same, especially when dealing with the Twitter API.


## Examples

The scripts assume that there is a local file named **creds.tw.json** -- you'll have to make your own, but you can look at the [sample.creds.tw.json](sample.creds.tw.json) sample and fill it in with your own Twitter API keys.

When everything is setup, you should be able to do this (when running a script or iPython local to this directory):


###### Post a tweet 

via the [statuses/update](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update) endpoint

```py
import tyfoo
client = tyfoo.get_client()
tmeta = client.update_status(status='Hey I am tweeting from the API!')
```


##### Reply to a tweet

This also uses the [statuses/update](https://developer.twitter.com/en/docs/tweets/post-and-engage/api-reference/post-statuses-update) endpoint. However, replying to a tweet has a couple of requirements that a regular tweet does not:

- the `in_reply_to_status_id` parameter must be filled
- the text of your reply must contain the `@screen_name` of the user who authored the tweet you replied to.

For example, if you were to reply to this tweet:

https://twitter.com/realDonaldTrump/status/269184429849718784

Your call to `update_status()` would have at least these arguments:

```py
client.update_status(
  status='Abe was right! Good reference, @realDonaldTrump',
  in_reply_to_status_id=269184429849718784
)
```



### Code examples

[tyfoo.py](tyfoo.py) - contains some wrappers and helpers for quickly authenticating and doing some common tasks, like searching for Tweets, and
replying to tweets. However, I wrote it with the mindset of avoiding any use of object-oriented design, so it won't look very pretty...

- [example_send_tweet.py](example_send_tweet.py) - just a quick example of how to send a tweet using the [tyfoo.py](tyfoo.py) library/module
- [example_send_hellos.py](example_send_hellos.py) - why send just one tweet when we can send a series of them?
- [example_stanford_news.py](example_stanford_news.py) - An example of connecting one program -- a headline scraper -- and feeding into another: an automated tweeting program.
- [example_send_replies.py](example_send_replies.py) - A proof of concept showing how bots like [@StealthMountain](http://www.craveonline.com/site/180711-8-angry-conversations-with-stealth-mountain) do their thing.



