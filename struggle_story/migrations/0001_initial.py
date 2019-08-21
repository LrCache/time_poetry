# -*- coding: utf-8 -*-
# Generated by Django 1.11.21 on 2019-08-08 15:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.TextField(default='new article', max_length=256)),
                ('sub_title', models.TextField(max_length=256, null=True)),
                ('tag_type', models.IntegerField(default=0, max_length=1)),
                ('summary', models.TextField(max_length=256, null=True)),
                ('content', models.TextField(default='this is an article!')),
                ('author_id', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('publish_time', models.DateTimeField(auto_now=True)),
                ('last_update_time', models.DateTimeField(auto_now=True)),
                ('publish_state', models.IntegerField(default=True, max_length=1)),
                ('category_id', models.IntegerField(default=0)),
            ],
        ),
    ]
