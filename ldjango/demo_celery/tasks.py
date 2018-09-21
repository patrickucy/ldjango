# coding=utf-8
import time
from celery import shared_task


@shared_task
def send_email(mail):
    print('sending mail ...' + mail['to'])
    time.sleep(3.0)
    print('mail sent.')
    return "rst: mail sent"


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
