from django.shortcuts import render, HttpResponse
from .tasks import async_task_add


# Create your views here.
def index(request):
    return HttpResponse("Index page of demo_celery")


def test(request):
    print("celery test: ")
    return HttpResponse("celery test: ")


