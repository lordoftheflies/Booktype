# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-10-31 17:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editor', '0010_auto_20170908_0624'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='checked_statuses',
            field=models.ManyToManyField(related_name='checked_statuses', to='editor.BookStatus'),
        ),
    ]
