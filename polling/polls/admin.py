from django.contrib import admin

from .models import *


class PollsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Polls._meta.fields]


admin.site.register(Polls, PollsAdmin)


class UserModelAdmin(admin.ModelAdmin):
    list_display = [f.name for f in UserModel._meta.fields]


admin.site.register(UserModel, UserModelAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Question._meta.fields]


admin.site.register(Question, QuestionAdmin)
