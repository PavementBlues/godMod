from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Subreddit(models.Model):
    subID = models.IntegerField(primary_key=True)
    datetimeViewed = models.DateTimeField
    name = models.CharField
    subscriberCount = models.IntegerField
    datetimeFounded = models.DateTimeField

    def __str__(self):
        return self.name

class Redditor(models.Model):
    redditorID = models.IntegerField(primary_key=True)
    name = models.CharField
    linkKarma = models.IntegerField
    commentKarma = models.IntegerField
    datetimeViewed = models.DateTimeField

    def __str__(self):
        return self.name

class SubModerator(models.Model):
    moderatorID = models.IntegerField(primary_key=True)
    subreddit = models.ForeignKey(Subreddit, on_delete=models.CASCADE)
    redditor = models.ForeignKey(Redditor, on_delete=models.CASCADE)
    ranking = models.IntegerField
    dateModded = models.DateTimeField

    def __str__(self):
        return self.redditor.name

class Post(models.Model):
    postID = models.IntegerField(primary_key=True)
    datetimeViewed = models.DateTimeField
    subreddit = models.ForeignKey(Subreddit, on_delete=models.CASCADE)
    author = models.ForeignKey(Redditor, on_delete=models.CASCADE)
    timePosted = models.DateTimeField
    title = models.CharField
    body = models.CharField
    score = models.IntegerField
    editedYN = models.CharField(max_length=1)
    gildedCount = models.IntegerField

    def __str__(self):
        return self.body

class Comment(models.Model):
    commentID = models.IntegerField(primary_key=True)
    datetimeViewed = models.DateTimeField
    subreddit = models.ForeignKey(Subreddit, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    redditor = models.ForeignKey(Redditor, on_delete=models.CASCADE)
    datetimePosted = models.DateTimeField
    body = models.CharField
    score = models.IntegerField
    editedYN = models.CharField(max_length=1)
    gildedCount = models.IntegerField

    def __str__(self):
        return self.body

class CommentResponse(models.Model):
    commentResponseID = models.IntegerField(primary_key=True)
    originalComment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="original")
    respondingComment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="responding")

class User(models.Model):
    userID = models.IntegerField(primary_key=True)
    redditAccount = models.OneToOneField(Redditor, on_delete=models.CASCADE, verbose_name="reddit account for system user")
    name = models.CharField

    def __str__(self):
        return self.name

class ItemType(models.Model):
    itemTypeID = models.IntegerField(primary_key=True)
    description = models.CharField

    def __str__(self):
        return self.description

class ItemStatus(models.Model):
    itemStatusID = models.IntegerField(primary_key=True)
    description = models.CharField

    def __str__(self):
        return self.description

class WorkItem(models.Model):
    workItemID = models.IntegerField(primary_key=True)
    title = models.CharField
    body = models.CharField
    userAssigned = models.ForeignKey(User, on_delete=models.CASCADE)
    itemType = models.ForeignKey(ItemStatus, on_delete=models.CASCADE)
    itemStatus = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    topLevelYN = models.CharField(max_length=1)

    def __str__(self):
        return self.title

class ItemComment(models.Model):
    itemCommentID = models.IntegerField(primary_key=True)
    workItem = models.ForeignKey(WorkItem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.CharField
    
    def __str__(self):
        return self.body

class ItemCommentResponse(models.Model):
    itemCommentResponse = models.IntegerField(primary_key=True)
    originalComment = models.ForeignKey(User, on_delete=models.CASCADE, related_name="original")
    respondingComment = models.ForeignKey(User, on_delete=models.CASCADE, related_name="responding")


class Report(models.Model):
    reportID = models.IntegerField(primary_key=True)
    reportedComment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reportedRedditor = models.ForeignKey(Redditor, on_delete=models.CASCADE, related_name="reported")
    reportingRedditor = models.ForeignKey(Redditor, on_delete=models.CASCADE, related_name="reporting")
    reason = models.CharField

    def __str__(self):
        return self.reason

