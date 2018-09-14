# coding=utf-8
from celery import shared_task


@shared_task
def async_task_add(x, y):
    print("async_add()")
    return x + y


@shared_task
def async_task_mul(x, y):
    return x * y


@shared_task
def async_task_xsum(numbers):
    return sum(numbers)

