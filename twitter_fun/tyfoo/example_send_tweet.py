# Simple example of sending tweet

import tyfoo

# get an api handle (i.e client)
me = tyfoo.get_client()
my_name = me.auth.get_username()
print('You have authenticated as: ', my_name)

msg = """Today feels pretty good! Check out the weather:
https://www.accuweather.com/"""

t = me.update_status(status=msg)
# t is a Tweet object, but I prefer having it as a dict
tweet = t._json

print(tweet['id'])
print(tweet['created_At'])
