from django.urls import path

from . import views

app_name = "demo_celery"

urlpatterns = [
    path(r'', views.index),
    path(r'test/', views.test)
]

