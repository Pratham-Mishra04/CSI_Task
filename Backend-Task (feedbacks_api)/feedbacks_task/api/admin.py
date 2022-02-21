from django.contrib import admin
from .models import Feedback
# Register your models here.

class FeedbackAdmin(admin.ModelAdmin):
    fields=['id','name','feed','time']

admin.site.register(Feedback,FeedbackAdmin)