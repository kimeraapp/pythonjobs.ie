from pythonjobs.celery import app
from pythonjobs.services import Twitter


@app.task
def tweet(job_id):
    print("HEEEEEEEEEEEEEEERE " + str(job_id))
    twitter = Twitter()
    twitter.tweet(str(job_id))
