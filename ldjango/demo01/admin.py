from django.contrib import admin
from .models import Question
from .models import Choice

# Register your models here.
admin.site.register(Question)  # register My app models for admin sys
admin.site.register(Choice)  # register My app models for admin sys
