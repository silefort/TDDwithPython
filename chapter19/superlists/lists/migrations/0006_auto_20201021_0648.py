# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-10-21 06:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0005_auto_20201011_1552'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('id',)},
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together=set([('list', 'text')]),
        ),
    ]