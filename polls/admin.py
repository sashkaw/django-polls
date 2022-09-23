from django.contrib import admin

from .models import Choice, Question

# Register your models here.

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3

class QuestionAdmin(admin.ModelAdmin):

  list_display = ("question_text", "pub_data", "was_published_recently")
  list_filter = ["pub_data"]
  search_fields = ["question_text"]

  #fields = ["pub_data", "question_text"]
  
  fieldsets = [
    (None, {"fields": ["question_text"]}),
    #("Date information", {"fields": ["pub_data"]}),
    ("Date information", {"fields": ["pub_data"], "classes": ["collapse"]}), #the collapse bit just hides the data info on the UI
  ]
  inlines = [ChoiceInline]



admin.site.register(Question, QuestionAdmin)
#admin.site.register(Choice)