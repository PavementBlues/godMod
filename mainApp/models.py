from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Subreddit(models.Model):
    subID = models.IntegerField(primary_key=True, default=1)
    datetimeViewed = models.DateTimeField(auto_now=True, null=True)
    name = models.CharField(max_length=100, default="")
    subscriberCount = models.IntegerField(null=True)
    datetimeFounded = models.DateTimeField(auto_now=False, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "subreddit"

class Redditor(models.Model):
    redditorID = models.IntegerField(primary_key=True, default=1)
    name = models.CharField(max_length=100, default="")
    linkKarma = models.IntegerField(null=True)
    commentKarma = models.IntegerField(null=True)
    datetimeViewed = models.DateTimeField(auto_now=False, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "redditor"

class Moderator(models.Model):
    moderatorID = models.IntegerField(primary_key=True, default=1)
    subreddit = models.ForeignKey(Subreddit, on_delete=models.CASCADE)
    redditor = models.ForeignKey(Redditor, on_delete=models.CASCADE)
    ranking = models.IntegerField(null=True)
    dateModded = models.DateTimeField(auto_now=False, null=True)

    def __str__(self):
        return self.redditor.name

    class Meta:
        db_table = "moderator"

class Post(models.Model):
    postID = models.IntegerField(primary_key=True, default=1)
    datetimeViewed = models.DateTimeField(auto_now=True, null=True)
    subreddit = models.ForeignKey(Subreddit, on_delete=models.CASCADE)
    author = models.ForeignKey(Redditor, on_delete=models.CASCADE)
    timePosted = models.DateTimeField(auto_now=False, null=True)
    title = models.CharField(max_length=300, default="")
    body = models.TextField(max_length=40000, default="")
    score = models.IntegerField(null=True)
    editedYN = models.CharField(max_length=1, default="")
    gildedCount = models.IntegerField(null=True)

    def __str__(self):
        return self.body

    class Meta:
        db_table = "post"

class Comment(models.Model):
    commentID = models.IntegerField(primary_key=True, default=1)
    datetimeViewed = models.DateTimeField(auto_now=True, null=True)
    subreddit = models.ForeignKey(Subreddit, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    redditor = models.ForeignKey(Redditor, on_delete=models.CASCADE)
    datetimePosted = models.DateTimeField(auto_now=False, null=True)
    body = models.TextField(max_length=40000, default="")
    score = models.IntegerField(null=True)
    editedYN = models.CharField(max_length=1, default="")
    gildedCount = models.IntegerField(null=True)

    def __str__(self):
        return self.body

    class Meta:
        db_table = "comment"

class CommentResponse(models.Model):
    commentResponseID = models.IntegerField(primary_key=True, default=1)
    originalComment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="original")
    respondingComment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="responding")

    class Meta:
        db_table = "commentResponse"

class User(models.Model):
    userID = models.IntegerField(primary_key=True, default=1)
    redditAccount = models.OneToOneField(Redditor, on_delete=models.CASCADE, verbose_name="reddit account for system user")
    name = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "user"

class ItemType(models.Model):
    itemTypeID = models.IntegerField(primary_key=True, default=1)
    description = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.description

    class Meta:
        db_table = "itemType"

class ItemStatus(models.Model):
    itemStatusID = models.IntegerField(primary_key=True, default=1)
    description = models.CharField(max_length=50, default="")

    def __str__(self):
        return self.description

    class Meta:
        db_table = "itemStatus"

class WorkItem(models.Model):
    workItemID = models.IntegerField(primary_key=True, default=1)
    title = models.CharField(max_length=300, default="")
    body = models.TextField(max_length=40000, default="")
    userAssigned = models.ForeignKey(User, on_delete=models.CASCADE)
    itemType = models.ForeignKey(ItemStatus, on_delete=models.CASCADE)
    itemStatus = models.ForeignKey(ItemType, on_delete=models.CASCADE)
    topLevelYN = models.CharField(max_length=1, default="")

    def __str__(self):
        return self.title

    class Meta:
        db_table = "workItem"

class ItemComment(models.Model):
    itemCommentID = models.IntegerField(primary_key=True, default=1)
    workItem = models.ForeignKey(WorkItem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=40000, default="")
    datetimePosted = models.DateTimeField(auto_now=False, null=True)
    
    def __str__(self):
        return self.body

    class Meta:
        db_table = "itemComment"

class ItemCommentResponse(models.Model):
    itemCommentResponse = models.IntegerField(primary_key=True, default=1)
    originalComment = models.ForeignKey(User, on_delete=models.CASCADE, related_name="original")
    respondingComment = models.ForeignKey(User, on_delete=models.CASCADE, related_name="responding")

    class Meta:
        db_table = "itemCommentResponse"

class Report(models.Model):
    reportID = models.IntegerField(primary_key=True, default=1)
    reportedComment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    reportedRedditor = models.ForeignKey(Redditor, on_delete=models.CASCADE, related_name="reported")
    reportingRedditor = models.ForeignKey(Redditor, on_delete=models.CASCADE, related_name="reporting")
    reason = models.TextField(max_length=1000, default="")
    datetimeReported = models.DateTimeField(auto_now=False, null=True)

    def __str__(self):
        return self.reason

    class Meta:
        db_table = "report"

