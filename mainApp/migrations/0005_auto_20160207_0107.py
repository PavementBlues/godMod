# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-07 01:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainApp', '0004_auto_20160207_0106'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editedYN', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='CommentResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('originalComment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='original', to='mainApp.Comment')),
                ('respondingComment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responding', to='mainApp.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='ItemComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ItemCommentResponse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ItemStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ItemType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('editedYN', models.CharField(max_length=1)),
            ],
        ),
        migrations.CreateModel(
            name='Redditor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reportedComment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Comment')),
                ('reportedRedditor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reported', to='mainApp.Redditor')),
                ('reportingRedditor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reporting', to='mainApp.Redditor')),
            ],
        ),
        migrations.CreateModel(
            name='SubModerator',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('redditor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Redditor')),
            ],
        ),
        migrations.CreateModel(
            name='Subreddit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('redditAccount', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Redditor', verbose_name='reddit account for system user')),
            ],
        ),
        migrations.CreateModel(
            name='WorkItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topLevelYN', models.CharField(max_length=1)),
                ('itemStatus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.ItemType')),
                ('itemType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.ItemStatus')),
                ('userAssigned', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.User')),
            ],
        ),
        migrations.AddField(
            model_name='submoderator',
            name='subreddit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Subreddit'),
        ),
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Redditor'),
        ),
        migrations.AddField(
            model_name='post',
            name='subreddit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Subreddit'),
        ),
        migrations.AddField(
            model_name='itemcommentresponse',
            name='originalComment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='original', to='mainApp.User'),
        ),
        migrations.AddField(
            model_name='itemcommentresponse',
            name='respondingComment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='responding', to='mainApp.User'),
        ),
        migrations.AddField(
            model_name='itemcomment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.User'),
        ),
        migrations.AddField(
            model_name='itemcomment',
            name='workItem',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.WorkItem'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Post'),
        ),
        migrations.AddField(
            model_name='comment',
            name='redditor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Redditor'),
        ),
        migrations.AddField(
            model_name='comment',
            name='subreddit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainApp.Subreddit'),
        ),
    ]
