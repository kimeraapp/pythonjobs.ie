from pythonjobs.celery import app


@app.task
def tweet():
    print("HEEEEEEEEEEEEEEERE")
