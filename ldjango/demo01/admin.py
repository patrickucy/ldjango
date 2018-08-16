from django.contrib import admin
from .models import Question
from .models import Choice


# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 1  # by default, providing  1 or more choices.


class QuestionAdmin(admin.ModelAdmin):
    # Question detail display
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInline]

    # Question display
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']


admin.site.register(Question, QuestionAdmin)  # register My app models for admin sys
admin.site.register(Choice)  # register My app models for admin sys
