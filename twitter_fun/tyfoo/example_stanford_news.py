import requests
from tyfoo import get_client
from bs4 import BeautifulSoup
from time import sleep

STANFORD_NEWS_URL = 'https://www.stanford.edu/news/'
TEST_NEWS_URL = 'https://wgetsnaps.github.io/stanford-edu-news/news/'
TEST_SIMPLE_URL = 'https://wgetsnaps.github.io/stanford-edu-news/news/simple.html'

TWEET_TEMPLATE = """{title}
via @Stanford: {url}
🌲  🌲  🌲 #Stanford"""



def get_stanford_headlines(url):
    """
    Fetches from `url`

    Returns a list of dictionaries:
    [
        {'url': 'https://news.stanford.edu/2018/01/23/insects-took-off-evolved-wings/',
         'title': 'Insects took off when they evolved wings'}
    ]

    """
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, 'lxml')
    tags = soup.select('h3 > a')

    headlines = []
    for t in tags:
        h = {}
        h['url'] = t.attrs['href']
        h['title'] = t.text
        headlines.append(h)

    return headlines



def create_story_tweets(headlines):
    """
    headlines is a list of dicts

    Returns a list of strings. Each string contains
      a message properly formatted for sending out
      as a tweet
    """

    tweettexts = []

    for h in headlines:
        txt = TWEET_TEMPLATE.format(title=h['title'], url=h['url'])
        tweettexts.append(txt)

    return tweettexts



def tweet_stanford_stories(url=STANFORD_NEWS_URL, dryrun=False, sleeptime=5):
    heds = get_stanford_headlines(url)
    texts = create_story_tweets(heds)
    if dryrun:
       for txt in texts:
         print('\n\nDryrun tweet:')
         print(txt)
    else:
        # get the twitter stuff going
        client = get_client()
        for txt in texts:
            t = client.update_status(status=txt)
            print('Sent tweet {id}:\n{text}'.format(id=t.id, text=t.text))
            sleep(sleeptime)


