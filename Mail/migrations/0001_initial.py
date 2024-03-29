# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-29 17:48
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('People', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty_Student_Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000)),
                ('facultyID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='People.Faculty')),
                ('studentID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='People.Student')),
            ],
        ),
        migrations.CreateModel(
            name='Student_Faculty_Mail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.CharField(max_length=1000)),
                ('facultyID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='People.Faculty')),
                ('studentID', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='People.Student')),
            ],
        ),
    ]
