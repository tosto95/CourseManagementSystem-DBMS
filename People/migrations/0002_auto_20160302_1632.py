# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-02 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('People', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='adminPassword',
            field=models.CharField(max_length=100, verbose_name='Login Password'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='adminUserName',
            field=models.CharField(max_length=100, verbose_name='Login Username'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='firstName',
            field=models.CharField(max_length=100, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='admin',
            name='lastName',
            field=models.CharField(max_length=100, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='dob',
            field=models.DateField(verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='facultyPassword',
            field=models.CharField(max_length=100, verbose_name='Login Password'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='facultyUserName',
            field=models.CharField(max_length=100, verbose_name='Login Username'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='firstName',
            field=models.CharField(max_length=100, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='lastName',
            field=models.CharField(max_length=100, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='firstName',
            field=models.CharField(max_length=100, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='lastName',
            field=models.CharField(max_length=100, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='parentPassword',
            field=models.CharField(max_length=100, verbose_name='Login Password'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='parentUserName',
            field=models.CharField(max_length=100, verbose_name='Login Username'),
        ),
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='student',
            name='firstName',
            field=models.CharField(max_length=100, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='lastName',
            field=models.CharField(max_length=100, verbose_name='Last Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentPassword',
            field=models.CharField(max_length=100, verbose_name='Login Password'),
        ),
        migrations.AlterField(
            model_name='student',
            name='studentUserName',
            field=models.CharField(max_length=100, verbose_name='Login Username'),
        ),
    ]
