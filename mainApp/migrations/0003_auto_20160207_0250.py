# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-07 02:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0002_auto_20160207_0207'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='body',
            field=models.TextField(default='', max_length=40000),
        ),
        migrations.AddField(
            model_name='comment',
            name='datetimePosted',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='datetimeViewed',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='gildedCount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='score',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='itemcomment',
            name='body',
            field=models.TextField(default='', max_length=40000),
        ),
        migrations.AddField(
            model_name='itemcomment',
            name='datetimePosted',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='itemstatus',
            name='description',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='itemtype',
            name='description',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='moderator',
            name='dateModded',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='moderator',
            name='ranking',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='body',
            field=models.TextField(default='', max_length=40000),
        ),
        migrations.AddField(
            model_name='post',
            name='datetimeViewed',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='gildedCount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='score',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='timePosted',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AddField(
            model_name='redditor',
            name='commentKarma',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='redditor',
            name='datetimeViewed',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='redditor',
            name='linkKarma',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='redditor',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='report',
            name='datetimeReported',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='report',
            name='reason',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='subreddit',
            name='datetimeFounded',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='subreddit',
            name='datetimeViewed',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='subreddit',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='subreddit',
            name='subscriberCount',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='workitem',
            name='body',
            field=models.TextField(default='', max_length=40000),
        ),
        migrations.AddField(
            model_name='workitem',
            name='title',
            field=models.CharField(default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='comment',
            name='editedYN',
            field=models.CharField(default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='editedYN',
            field=models.CharField(default='', max_length=1),
        ),
        migrations.AlterField(
            model_name='workitem',
            name='topLevelYN',
            field=models.CharField(default='', max_length=1),
        ),
    ]
