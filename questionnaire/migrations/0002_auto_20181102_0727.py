# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-02 05:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaire', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='techer',
            name='m_sDiscipline',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.Discipline'),
        ),
    ]
