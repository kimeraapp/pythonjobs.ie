import string
import random
from django.core.mail import send_mail
from django.template import loader
import tweepy

from jobs.models import Job
from pythonjobs import settings


class Twitter(object):
        def __init__(self):
            self.consumer_key = settings.TWITTER_KEY
            self.consumer_secret = settings.TWITTER_SECRET
            self.token = settings.TWITTER_ACCESS_TOKEN
            self.token_secret = settings.TWITTER_TOKEN_SECRET
            auth = tweepy.OAuthHandler(self.consumer_key,
                                       self.consumer_secret)
            auth.set_access_token(self.token, self.token_secret)

            self.api = tweepy.API(auth)

        def tweet(self, message):
            return self.api.update_status(status=message)


def generate_token(length=60):
    chars = string.ascii_uppercase + string.digits
    token = ''.join(random.choice(chars) for _ in range(length))
    while Job.objects.filter(token=token).exists():
        token = generate_token()
    return token


def send_confirmation_mail(job):
    subject = "You just posted a job on pythonjobs.ie"
    template = loader.get_template("email.html")
    body = template.render({'job': job})
    to_email = [job.email]
    from_email = "info@kimera.io"

    return send_mail(subject, body, from_email, to_email,
                     fail_silently=True, html_message=body)
