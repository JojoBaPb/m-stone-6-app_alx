from celery import shared_task
from django.core.mail import send_mail

@shared_task
def add(x, y):
    return x + y

@shared_task
def send_test_email(to_email):
    send_mail('Hello from m6_app', 'This is a test', None, [to_email], fail_silently=False)
    return True

