import config
import smtplib

class Emailer(object):
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.email = user.join(config.EMAILER_SUFFIX)
        self.server = smtplib.SMTP(config.EMAILER_SERVER, config.EMAILER_PORT)

    def __enter__(self):
        self.server.ehlo()
        self.server.starttls()
        self.server.login(self.user, self.password)
        return self

    def __exit__(self, type, value, traceback):
        self.server.close()

    def send_email(self, e_to=None, msg=None):
        self.server.sendmail(
            self.email,
            e_to if e_to else self.email,
            msg if msg else "Empty email"
        )
