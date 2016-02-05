from django.contrib import admin
from .models import *

# Register your models here.

mainAppModels = [Subreddit, Redditor, SubModerators, Post, Comment,
	CommentResponses, User, Discussion, Report]
admin.site.register(mainAppModels)
