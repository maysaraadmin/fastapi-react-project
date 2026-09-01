from celery import Celery

celery_app = Celery(
    "worker",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379/0",
)

celery_app.conf.task_routes = {"app.tasks.*": "main-queue"}
celery_app.conf.worker_send_task_events = True
celery_app.conf.task_send_sent_event = True
