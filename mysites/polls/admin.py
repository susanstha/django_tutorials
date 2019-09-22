from django.contrib import admin
from .models import Question
from .models import Answer
# Register your models here.


class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [AnswerInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    search_fields = ['question_text']
    list_filter = ['pub_date']
admin.site.register(Question, QuestionAdmin)

# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]
#
# admin.site.register(Question, QuestionAdmin)
#
# admin.site.register(Answer)
