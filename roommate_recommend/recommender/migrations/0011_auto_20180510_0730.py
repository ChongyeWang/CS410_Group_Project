# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-10 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recommender', '0010_auto_20180510_0355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='roommatepreference',
            name='gender_prefer',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1),
        ),
    ]
