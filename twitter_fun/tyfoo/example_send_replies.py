# pick a user to cheer their day via a few positive replies!

import random
import tyfoo
from time import sleep

TWEET_URL_BASE = 'https://twitter.com/{x}/status/{y}'
MESSAGES = ['Thanks for mentioning this!',
  "This was good to know",
  "Really interesting, can't wait for more developments!",
  "You made a positive impact on me. Cheers! :)",]

# get an api handle (i.e client)
me = tyfoo.get_client()
my_name = me.auth.get_username()
print('You have authenticated as: ', my_name)

# might as well set the username here
other_username = 'dancow'
# how many replies to send?
rep_count = 3

# get at least `rep_count` worth of tweets, and then some:
other_tweets = tyfoo.read_user_tweets( client=me,
                                       screen_name=other_username,
                                       count=rep_count+random.randint(5,30))

print('Fetched', len(other_tweets), 'tweets from', other_username)


# now pick a random set of tweets to reply to:
some_tweets = random.sample(other_tweets, rep_count)


for xt in some_tweets:
  # pick a random message
  msg = random.choice(MESSAGES)

  t_meta = tyfoo.send_reply(client=me, reply_text=msg,
                            target_tweet=xt)
  # send_reply() sends out its own meta info

  zsec = random.randint(2, 8)
  print('\nSleeping for', zsec, 'seconds...')
  sleep(zsec)
