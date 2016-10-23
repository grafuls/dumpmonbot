from tweepy import API
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

import config
import logging
import os
import re
import urllib2

LOGGER = logging.getLogger(__name__)


class listener(StreamListener):
    def on_error(self, status):
        print status

    def on_status(self, status):
        url = status._json['entities']['urls'][0]['expanded_url']
        html_content = urllib2.urlopen(url).read()
        regex = '(?:\A|(?<=.))[^.]*%s[^.]*(?:.|\Z)' % config.QUERY
        matches = re.findall(regex, html_content, 0)
        if len(matches) > 0:
            LOGGER.info("YOU HAVE BEEN PWND (potentially)")
            LOGGER.info("Source: %s:", url)
            for match in matches:
                LOGGER.info(match)


if __name__ == "__main__":
    auth = OAuthHandler(config.C_KEY, config.C_SECRET)
    auth.set_access_token(config.A_TOKEN, config.A_SECRET)
    api = API(auth)

    user = api.get_user(config.T_USER)
    user_id = str(user.id)

    twitterStream = Stream(auth, listener())
    twitterStream.filter(follow=[user_id])
