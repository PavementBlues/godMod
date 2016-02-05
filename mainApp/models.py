from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Subreddit(models.Model):
    subUid = models.IntegerField(primary_key=True)
    subDatetimeViewed = models.DateTimeField
    subName = models.CharField
    subSubscriberCount = models.IntegerField
    subDatetimeFounded = models.DateTimeField

    def __str__(self):
        return self.subName

class Redditor(models.Model):
    rdtUid = models.IntegerField
    rdtName = models.CharField
    rdtLinkKarma = models.IntegerField
    rdtCommentKarma = models.IntegerField
    rdtDatetimeViewed = models.DateTimeField

class SubModerator(models.Model):
    sumUid = models.IntegerField(primary_key=True)
    sumSubUid = models.ForeignKey(Subreddit, on_delete=models.CASCADE)
    sumRdtUid = models.ForeignKey(Redditor, on_delete=models.CASCADE)
    sumRanking = models.IntegerField
    sumDateModded = models.DateTimeField

    def __str__(self):
        return self.sumRdtUid

class Post(models.Model):
    pstUid = models.IntegerField(primary_key=True)
    pstDatetimeViewed = models.DateTimeField
    pstSubUid = models.ForeignKey(Subreddit, on_delete=models.CASCADE)
    pstRdtUidAuthor = models.ForeignKey(Redditor, on_delete=models.CASCADE)
    pstDatetimePosted = models.DateTimeField
    pstTitle = models.CharField
    pstBody = models.CharField
    pstScore = models.IntegerField
    pstEditedYN = models.CharField(max_length=1)
    pstGildedCount = models.IntegerField

    def __str__(self):
        return self.pstBody

class Comment(models.Model):
    cmtUid = models.IntegerField(primary_key=True)
    cmtDatetimeViewed = models.DateTimeField
    cmtSubUid = models.ForeignKey(Subreddit, on_delete=models.CASCADE)
    cmtPstUid = models.ForeignKey(Post, on_delete=models.CASCADE)
    cmtRdtUidAuthor = models.ForeignKey(Redditor, on_delete=models.CASCADE)
    cmtDatetimePosted = models.DateTimeField
    cmtBody = models.CharField
    cmtScore = models.IntegerField
    cmtEditedYN = models.CharField(max_length=1)
    cmtGildedCount = models.IntegerField

    def __str__(self):
        return self.cmtBody

class CommentResponse(models.Model):
    cmrUid = models.IntegerField(primary_key=True)
    cmrCmtUidOP = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="original")
    cmrCmtUidResponder = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="responding")

    def __str__(self):
        return self.cmrUid

class User(models.Model):
    usrUid = models.IntegerField(primary_key=True)
    usrRdtUid = models.OneToOneField(Redditor, on_delete=models.CASCADE, verbose_name="reddit account for system user")

    def __str__(self):
        return self.subName

class Discussion(models.Model):
    dscUid = models.IntegerField(primary_key=True)
    dscUsrUid = models.ForeignKey(User, on_delete=models.CASCADE)
    dscTitle = models.CharField
    dscBody = models.CharField
    dscTopLevelYN = models.CharField(max_length=1)

    def __str__(self):
        return self.dscTitle

class Report(models.Model):
    rptUid = models.IntegerField(primary_key=True)
    rptCmtUid = models.ForeignKey(Comment, on_delete=models.CASCADE)
    rptRdtUidReporter = models.ForeignKey(Redditor, on_delete=models.CASCADE, related_name="reporting")
    rptRdtUidReportee = models.ForeignKey(Redditor, on_delete=models.CASCADE, related_name="reported")
    rptReason = models.CharField

    def __str__(self):
        return self.rptReason

