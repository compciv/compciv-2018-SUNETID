import random
import tyfoo
from time import sleep

SALUTATIONS = ['Hello, world!', 'Carpe Diem!', 'I ♥ Applebees']
SENTENCES = ['I am hungry for food and knowledge', "Best wishes!",
            "Shiny happy people everywhere!",
            'Unpossible is nothing.']
EMOTES = ['😊', '😀', '🤗', '😎', '😽', '🖖']

TWEET_URL_BASE = 'https://twitter.com/{x}/status/{y}'

me = tyfoo.get_client()
my_name = me.auth.get_username()
print('You have authenticated as: ', my_name)
################

hello_count = 3

print("\n\nSending out", hello_count, "messages!")

for i in range(hello_count):
  mx = []
  mx.append(random.choice(SALUTATIONS))
  mx.append(random.choice(SENTENCES))
  mx.append(random.choice(EMOTES))

  msg = ' '.join(mx)

  # send out the tweet
  rx = me.update_status(status=msg)
  t_meta = rx._json
  tweet_url = TWEET_URL_BASE.format(x=my_name, y=t_meta['id'])

  # some meta info to print out
  print('------------')
  print("Tweet number", i)
  print(tweet_url)
  print(t_meta['text'])

  zsec = random.randint(2, 8)
  print('\nSleeping for', zsec, 'seconds...\n\n\n')
  sleep(zsec)
