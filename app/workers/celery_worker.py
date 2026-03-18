from celery import Celery
from app.services.extractor import extract_content
from app.core.config import settings

celery = Celery(
    "worker",
    broker=settings.CELERY_BROKER_URL,
    backend=settings.CELERY_RESULT_BACKEND
)


@celery.task(bind=True)
def extract_task(self, url):
    return extract_content(url)
