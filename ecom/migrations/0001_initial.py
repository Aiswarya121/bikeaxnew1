# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-18 09:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Description', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Image', models.FileField(blank=True, null=True, upload_to='media/')),
                ('IDorSNO', models.IntegerField()),
                ('Description', models.TextField(max_length=50)),
                ('Price', models.IntegerField()),
                ('NumbersAvailable', models.IntegerField()),
                ('Categories', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ecom.Category')),
            ],
        ),
    ]
