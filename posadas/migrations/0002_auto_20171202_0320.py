# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-02 03:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posadas', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posada',
            old_name='hora',
            new_name='fecha_hora',
        ),
        migrations.RemoveField(
            model_name='posada',
            name='fecha',
        ),
    ]