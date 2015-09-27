from pythonjobs.celery import app
from pythonjobs.services import Twitter


@app.task
def tweet(job_url):
    print("Sharing message on twitter")
    message = u"There is a new job on http://pythonjobs.ie{0} " \
        "#jobsearch #python #ireland".format(job_url)
    twitter = Twitter()
    twitter.tweet(message)
