from os.path import expanduser
import json
import tweepy
import re


DEFAULT_CREDS_FILENAME = expanduser('creds.tw.json')
DEBUG_REPLY_INFO = """
=======================================
Sending reply...

    user:
      https://twitter.com/{sn}

    tweet:
      https://twitter.com/{sn}/status/{id}

         {txt}


----------------------------------------


"""

def get_client(fname=DEFAULT_CREDS_FILENAME):
    client = _tw_authenticate_client(fname)
    return client


def search(client, query, result_type='recent'):
    tweets = client.search(q=query, count=100, result_type=result_type)
    return [t._json for t in tweets]


def read_user_tweets(client, screen_name, count=200, since_id=None):
    results = client.user_timeline(screen_name=screen_name,
                                 trim_user=True,
                                 exclude_replies=False,
                                 include_rts=False,
                                 count=count,
                                 since_id=since_id)
    # need to convert each result object into
    # a dict object. Also have to manually add user object
    # since we leave it out in the API call
    tweets = []
    for r in results:
        t = r._json
        t['user'] = {'screen_name': screen_name}
        tweets.append(t)
    return tweets



def send_reply(client, reply_text, target_tweet=None,
                       target_url=None, target_screen_name=None,
                       target_tweet_id=None,
                       debug_mode=False):

    if not (target_tweet or target_url) and not (target_screen_name and target_tweet_id):
        raise InputError('Must supply Tweet object, url, or target_screen_name and target_tweet_id')
    elif target_tweet:
        r_screen_name = target_tweet['user']['screen_name']
        r_tweet_id = target_tweet['id']
    elif target_url:
        _t = _tw_extract_data_from_tweet_url(target_url)
        r_screen_name = _t['screen_name']
        r_tweet_id = _t['tweet_id']
    else:
        r_screen_name = target_screen_name
        r_tweet_id = target_tweet_id

    r_text = _tw_build_reply_text(reply_text, r_screen_name)


    debugmsg = DEBUG_REPLY_INFO.format(sn=r_screen_name,
                                        id=r_tweet_id, txt=r_text)

    print(debugmsg)

    if debug_mode:
        print(':debug_mode arg set to True; not actually sending out reply')
        return False
    else:
        # #finally, sending it out
        result = client.update_status(status=r_text,
                             in_reply_to_status_id=r_tweet_id)

        return result

################
# helper functions



def _tw_authenticate_client(credsfilename):
    cf = expanduser(credsfilename)
    creds = json.load(open(cf))
    auth = tweepy.OAuthHandler(consumer_key = creds['consumer_key'],
                               consumer_secret = creds['consumer_secret'])
    auth.set_access_token(creds['access_token'],
                          creds['access_token_secret'])
    client = tweepy.API(auth)
    return client



def _tw_build_reply_text(status_text, target_screen_name):
    pattern = '@{sn} {txt}'
    txt = pattern.format(sn=target_screen_name, txt=status_text)
    return txt


def _tw_extract_data_from_tweet_url(url):
    """
    url (str): url of a tweet, e.g.
        'https://twitter.com/Stanford/status/953656911899086848'

    Returns: dict

        {
          'url': 'https://twitter.com/Stanford/status/953656911899086848',
          'screen_name': Stanford,
          'tweet_id': 953656911899086848,
        }"""


    mx = re.search('https://.*?twitter.com/@?(\w+)/status/(\d+)', url)
    if mx:
        h = {}
        h['url'] = url
        h['screen_name'] = mx[1]
        h['tweet_id'] = mx[2]
        return h
    else:
        raise InputError("Could not extract tweet info from url:", url)

"""
client = get_client()
tweets = search(client, '"less dogs"', count=200)
for t in tweets:



"""
