from pythonjobs.celery import app
from pythonjobs.services import Twitter


@app.task
def tweet(job):
    message = "New python job on {0}".format(job.get_absolute_url())
    twitter = Twitter()
    twitter.tweet(message)
