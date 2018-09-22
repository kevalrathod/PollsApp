from django.contrib import admin
from .models import Question,Choice


# Register your models here.



class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['que_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('que_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['que_text']




admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)