# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-12 23:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sabibatbet_forum', '0001_initial'),
        ('sabibatbet_menanggapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tanggapan',
            name='post_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='sabibatbet_forum.Post'),
        ),
    ]