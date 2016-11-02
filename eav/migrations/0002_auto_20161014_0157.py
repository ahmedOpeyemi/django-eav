# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-10-13 16:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('eav', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attribute',
            options={'ordering': ['content_type', 'name']},
        ),
        migrations.AddField(
            model_name='attribute',
            name='content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType', verbose_name='content type'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='display_order',
            field=models.PositiveIntegerField(default=1, verbose_name='display order'),
        ),
        migrations.AlterUniqueTogether(
            name='attribute',
            unique_together=set([('site', 'content_type', 'slug')]),
        ),
    ]
