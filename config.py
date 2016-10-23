import ConfigParser

EMAILER_SECTION = 'EMAILER'
TWEEPY_SECTION = 'TWEEPY'

conf_parser = ConfigParser.ConfigParser()
conf_parser.read('dumpmonbot.conf')

# EMAILER SECTION
EMAILER_SUFFIX = conf_parser.get(EMAILER_SECTION, 'SUFFIX')
EMAILER_SERVER = conf_parser.get(EMAILER_SECTION, 'SERVER')
EMAILER_PORT = conf_parser.get(EMAILER_SECTION, 'PORT')
EMAILER_USER = conf_parser.get(EMAILER_SECTION, 'USER')
EMAILER_PASS = conf_parser.get(EMAILER_SECTION, 'PASS')

# TWEEPY SECTION
C_KEY = conf_parser.get(TWEEPY_SECTION, 'C_KEY')
C_SECRET = conf_parser.get(TWEEPY_SECTION, 'C_SECRET')
A_TOKEN = conf_parser.get(TWEEPY_SECTION, 'A_TOKEN')
A_SECRET = conf_parser.get(TWEEPY_SECTION, 'A_SECRET')
T_USER = conf_parser.get(TWEEPY_SECTION, 'T_USER')
QUERY = conf_parser.get(TWEEPY_SECTION, 'QUERY')
