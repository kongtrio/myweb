# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-20 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('en_word', models.CharField(max_length=50)),
                ('cn_word', models.CharField(max_length=256)),
                ('en_spell', models.CharField(max_length=256)),
                ('sentence', models.TextField()),
                ('more_word', models.CharField(max_length=256)),
                ('opposites_word', models.CharField(max_length=256)),
            ],
        ),
    ]
