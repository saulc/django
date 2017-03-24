from django.contrib import admin

# Register your models here.
from .models import Question, Choice

# class ChoiceInline(admin.StackedInline):	# inline views
class ChoiceInline(admin.TabularInline):	# compact table of views
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
	fieldsets = [
	    (None,               {'fields': ['question_text']}),
	    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
	]
	inlines = [ChoiceInline]
	list_display = ('question_text', 'pub_date', 'was_published_recently')
	list_filter = ['pub_date']
	search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)



# admin.site.register(Question)
# admin.site.register(Choice)


# # class QuestionAdmin(admin.ModelAdmin):
# #     fields = ['pub_date', 'question_text']

# # admin.site.register(Question, QuestionAdmin)

# # feild sets
# class QuestionAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]

# admin.site.register(Question, QuestionAdmin)