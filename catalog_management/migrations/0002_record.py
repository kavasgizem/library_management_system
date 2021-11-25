# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-07-21 19:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog_management', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog_management.Book')),
                ('librarian', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='librarian', to=settings.AUTH_USER_MODEL)),
                ('patron', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Patron', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]