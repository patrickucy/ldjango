# coding=utf-8
import time
from celery import shared_task


@shared_task
def send_email(mail):
    print('sending mail ...' + mail['to'])
    time.sleep(2.0)
    print('mail sent.')


