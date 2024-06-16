from conf import app

@app.task
def add(x, y):
    return x + y


# celery -A task worker --loglevel=info
