from tweepy import API
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener

c_key = 'RhwBv3rqIMWWjCrNk4VAXysXm'
c_secret = '0E9EfIb92rOoka9qItLlVJ23kt9PpI5G6CJTdA8GHCVdQJmQPE'
a_token = '95932080-CgUYH2hwGBXt7CE4wCXL4bOHIuIcQhH7sJNxvZnSQ'
a_secret = 'bzZxOwh1xTnhnBFdGm8atTS2oLA8o45pS4H1eAnD2iEvI'

class listener(StreamListener):
    def on_error(self, status):
        print status

    def on_status(self, status):
        print status.text

auth = OAuthHandler(c_key, c_secret)
auth.set_access_token(a_token, a_secret)

api = API(auth)

user = api.get_user('grafuls08')
api.update_status('#dumpmon')

twitterStream = Stream(auth, listener())
twitterStream.filter(follow=[str(user.id)])

