# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-08 19:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0003_remove_registermodl_user_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registermodl',
            name='Profile_pic',
            field=models.FileField(blank=True, null=True, upload_to=b''),
        ),
    ]
