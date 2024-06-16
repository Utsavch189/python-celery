from celery import Celery

app = Celery('task', 
             broker='redis://localhost:6379/0', 
             backend='redis://localhost:6379/0',
             broker_connection_retry_on_startup=True
    )