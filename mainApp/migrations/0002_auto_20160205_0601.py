# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-05 06:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CommentResponses',
            new_name='CommentResponse',
        ),
        migrations.RenameModel(
            old_name='SubModerators',
            new_name='SubModerator',
        ),
    ]
