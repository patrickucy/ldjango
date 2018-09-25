# coding=utf-8
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from demo_celery import tasks
import celery
import redis


# Create your views here.
def index(request):
    return JsonResponse({
        "indexPage": "Index page of demo_celery"
    })


def test(request):
    rst = tasks.send_email.delay(dict(to='test@qq.com'))  # don't forget to use tasks.[task_name].delay([task_params])
    print(rst)
    return JsonResponse({
        "result": rst.task_id
    })


def test2(request):
    rids = redis.StrictRedis(host='127.0.0.1', port=6379)
    rids.set('name', 'jack')

    return JsonResponse({
        "test2": "test2"
    })
