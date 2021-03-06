# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-08 21:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0004_auto_20161108_1113'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registermodl',
            old_name='FirstName',
            new_name='Name',
        ),
        migrations.RemoveField(
            model_name='registermodl',
            name='LastName',
        ),
        migrations.AddField(
            model_name='registermodl',
            name='Bio',
            field=models.CharField(default=None, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registermodl',
            name='Gender',
            field=models.IntegerField(choices=[(1, b'Not Specified'), (2, b'Male'), (3, b'Female')], default=1),
        ),
        migrations.AddField(
            model_name='registermodl',
            name='Phone_number',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registermodl',
            name='Suggestions',
            field=models.BooleanField(default=1, verbose_name=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='registermodl',
            name='Website',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
