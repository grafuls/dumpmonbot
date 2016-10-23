from EmailManager import Emailer

import config

with Emailer(config.EMAILER_USER, config.EMAILER_PASS) as emailer:
    assert emailer.send_email(msg="MSG sent via %s" % __name__)
