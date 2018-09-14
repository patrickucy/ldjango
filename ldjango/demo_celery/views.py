from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from .tasks import send_email


# Create your views here.
def index(request):
    return JsonResponse({
        "indexPage": "Index page of demo_celery"
    })


def test(request):
    print("celery test: ")
    aysnc_rst = send_email.delay(dict(to='test@python.org'))
    return JsonResponse({
        "result": aysnc_rst
    })
