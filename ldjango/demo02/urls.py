from django.urls import path

from . import views

app_name = "demo02"
urlpatterns = [
    path(r'test.html', views.test),
    path(r'login.html', views.Login.as_view()),
    path(r'custom.html', views.custom),
    path(r'index.html', views.index)
]
