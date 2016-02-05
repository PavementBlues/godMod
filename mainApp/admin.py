from django.contrib import admin
from .models import *

# Register your models here.

mainAppModels = [Subreddit, Redditor, SubModerator, Post, Comment,
	CommentResponse, User, Discussion, Report]
admin.site.register(mainAppModels)
