from tweepy import API
# from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

import config
import os
import re
import urllib2
import logging

LOGGER = logging.getLogger("DUMPMON")
logging.basicConfig(level=logging.INFO, format='%(asctime)s |%(name)s| %(message)s')

class listener(StreamListener):
    def on_error(self, status):
        LOGGER.error(status)

    def on_status(self, status):
        LOGGER.info(status.text)


if __name__ == "__main__":
    USER = os.environ['T_USER']

    auth = OAuthHandler(config.C_KEY, config.C_SECRET)
    auth.set_access_token(config.A_TOKEN, config.A_SECRET)
    api = API(auth)

    status_id = 789360573788131328
    status = api.get_status(status_id)

    url = status._json['entities']['urls'][0]['expanded_url']
    html_content = urllib2.urlopen(url).read()
    query = 'chacha20-poly1305'
    # regex = '(?:\A|(?<=.))[^.]*%s[^.]*(?:.|\Z)' % query
    regex = '[^.]*%s[^.]*(?:.|\Z)' % query
    matches = re.findall(regex, html_content, 0)
    assert len(matches) > 0
    if len(matches) > 0:
        LOGGER.info("YOU HAVE BEEN PWND (potentially)")
        LOGGER.info("Source: %s", url)
        for match in matches:
            LOGGER.info(match)

    # user = api.get_user(USER)
    # user_id = str(user.id)

    # twitterStream = Stream(auth, listener())
    # twitterStream.filter(follow=[user_id])
