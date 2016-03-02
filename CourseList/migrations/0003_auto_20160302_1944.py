# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 14:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CourseList', '0002_auto_20160301_0059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courselist',
            old_name='faculty2',
            new_name='faculty',
        ),
        migrations.RemoveField(
            model_name='courselist',
            name='faculty1',
        ),
        migrations.AddField(
            model_name='studentregistration',
            name='grade',
            field=models.CharField(max_length=100, null=True, verbose_name='Grade'),
        ),
        migrations.AddField(
            model_name='studentregistration',
            name='progress',
            field=models.CharField(max_length=100, null=True, verbose_name='Progress'),
        ),
        migrations.AlterField(
            model_name='courselist',
            name='courseName',
            field=models.CharField(max_length=100, verbose_name='Course Name'),
        ),
        migrations.AlterField(
            model_name='studentregistration',
            name='courseID',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='CourseList.CourseList'),
        ),
    ]
