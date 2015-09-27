import string
import random
from django.core.mail import send_mail
from django.shortcuts import render
from django.template import loader


class Twitter(object):
    def tweet(msg):
        print(msg)


def generate_token(length=60):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(length))


def send_confirmation_mail(job):
    subject = "You just posted a job on pythonjobs.ie"
    template = loader.get_template("email.html")
    body = template.render({'job': job})
    to_email = [job.email]
    from_email = "info@kimera.io"

    return send_mail(subject, body, from_email, to_email,
                     fail_silently=True, html_message=body)
