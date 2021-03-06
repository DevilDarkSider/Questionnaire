# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-02 05:26
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_nScores1', models.IntegerField(default=0)),
                ('m_nScores2', models.IntegerField(default=0)),
                ('m_nScores3', models.IntegerField(default=0)),
                ('m_nScores4', models.IntegerField(default=0)),
                ('m_nScores5', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('m_sDiscipline', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('m_bGroup_F_11', models.BooleanField(default=False)),
                ('m_bGroup_M_12', models.BooleanField(default=False)),
                ('m_bGroup_I_13', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_sPassword', models.CharField(max_length=20)),
                ('m_sFullName', models.CharField(max_length=50)),
                ('m_sGroup', models.CharField(max_length=30)),
                ('m_sEmail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Techer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_sPassword', models.CharField(max_length=20)),
                ('m_sFullName', models.CharField(max_length=50)),
                ('m_sFaculty', models.CharField(max_length=30)),
                ('m_sDiscipline', models.CharField(max_length=50)),
                ('m_nRating', models.IntegerField(default=0)),
                ('m_sEmail', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='answer',
            name='m_sStEmail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.Student'),
        ),
        migrations.AddField(
            model_name='answer',
            name='m_sTeachEmail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaire.Techer'),
        ),
    ]
