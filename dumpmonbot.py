from EmailManager import Emailer
from tweepy import API
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

import config
import logging
import re
import requests

LOGGER = logging.getLogger("DUMPMON")
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s |%(name)s| %(message)s',
    filename='dumpmonbot.log'
)


class listener(StreamListener):
    def on_error(self, status):
        LOGGER.error(status)

    def on_status(self, status):
        LOGGER.info(status.text)
        url = status._json['entities']['urls'][0]['expanded_url']
        r = requests.get(url)
        if r.status_code == 200:
            regex = '[^\n]*%s[^\n]*(?:.)' % config.QUERY
            matches = re.findall(regex, r.text, 0)
            msg = []
            if len(matches) > 0:
                HEADER = "YOU HAVE BEEN PWND (potentially)"
                SOURCE_STRING = "Source: %s:"
                msg.append(HEADER)
                LOGGER.info(HEADER)
                msg.append(SOURCE_STRING % url)
                LOGGER.info(SOURCE_STRING, url)
                for match in matches:
                    msg.append(match)
                    LOGGER.info(match)
                with Emailer(config.EMAILER_USER, config.EMAILER_PASS) as emailer:
                    emailer.send_email(msg='\n'.join(msg))
        else:
            LOGGER.info("Failed to get content from %s", url)


if __name__ == "__main__":
    auth = OAuthHandler(config.C_KEY, config.C_SECRET)
    auth.set_access_token(config.A_TOKEN, config.A_SECRET)
    api = API(auth)

    user = api.get_user(config.T_USER)
    user_id = str(user.id)

    twitterStream = Stream(auth, listener())
    twitterStream.filter(follow=[user_id])
