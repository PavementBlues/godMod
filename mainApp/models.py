from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Subreddit(models.Model):
    subUid = models.IntegerField
    subDatetimeViewed = models.DateTimeField
    subName = models.CharField
    subSubscriberCount = models.IntegerField
    subDatetimeFounded = models.DateTimeField

class SubModerators(model.Model):
    sumUid = models.IntegerField
    sumSubUid = models.ForeignKey(Subreddit)
    sumRdtUid = models.ForeignKey(Redditor)
    sumRanking = models.IntegerField
    sumDateModded = models.DateTimeField

class Post(model.Model):
    pstUid = models.IntegerField
    pstDatetimeViewed = models.DateTimeField
    pstSubUid = models.ForeignKey(Subreddit)
    pstRdtUidAuthor = models.ForeignKey(Redditor)
    pstDatetimePosted = models.DateTimeField
    pstTitle = models.CharField
    pstBody = models.CharField
    pstScore = models.IntegerField
    pstEditedYN = models.CharField(max_length=1)
    pstGildedCount = models.IntegerField

class Comment(model.Model):
	cmtUid = models.IntegerField
	cmtDatetimeViewed = models.DateTimeField
	cmtSubUid = models.ForeignKey(Subreddit)
	cmtPstUid = models.ForeignKey(Post)
	cmtRdtUidAuthor = models.ForeignKey(Redditor)
	cmtDatetimePosted = models.DateTimeField
	cmtBody = models.CharField
	cmtScore = models.IntegerField
	cmtEditedYN = models.CharField(max_length=1)
	cmtGildedCount = models.IntegerField

class CommentResponses(model.Model):
	cmrUid = models.IntegerField
	cmrCmtUidOP = models.ForeignKey(Comment)
	cmrCmtUidResponder = models.ForeignKey(Comment)

class Redditor(model.Model):
	rdtUid = models.IntegerField
	rdtName = models.CharField
	rdtLinkKarma = models.IntegerField
	rdtCommentKarma = models.IntegerField
	rdtDatetimeViewed = models.DateTimeField

class User(models.Model):
    usrUid = models.IntegerField
    usrRdtUid = models.ForeignKey(Redditor)

class Discussion(models.Model):
	dscUid = models.IntegerField
	dscUsrUid = models.ForeignKey(User)
	dscPstUid = models.ForeignKey(Post)
	dscCmtUid = models.ForeignKey(Comment)
	dscTopLevelYN = models.CharField(max_length=1)

class Report(models.Model):
	rptUid = models.IntegerField
	rptCmtUid = models.ForeignKey(Comment)
	rptRdtUidReporter = models.ForeignKey(Redditor)
	rptRdtUidReportee = models.ForeignKey(Redditor)
	rptReason = models.CharField