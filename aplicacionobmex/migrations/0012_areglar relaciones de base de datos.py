# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 20:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacionobmex', '0011_auto_20170722_0016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contacto',
            name='pedido',
        ),
        migrations.RemoveField(
            model_name='institucion',
            name='contacto',
        ),
        migrations.RemoveField(
            model_name='institucion',
            name='pedido',
        ),
        migrations.AddField(
            model_name='contacto',
            name='institucion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacionobmex.Institucion'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='contacto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacionobmex.Contacto'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='institucion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacionobmex.Institucion'),
        ),
    ]
