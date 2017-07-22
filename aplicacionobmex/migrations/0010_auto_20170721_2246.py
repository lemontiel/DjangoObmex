# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-22 03:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacionobmex', '0009_auto_20170721_2218'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacto',
            name='comentarios',
            field=models.ManyToManyField(blank=True, to='aplicacionobmex.Comentario'),
        ),
        migrations.AddField(
            model_name='contacto',
            name='cursos',
            field=models.ManyToManyField(blank=True, to='aplicacionobmex.Curso'),
        ),
        migrations.AddField(
            model_name='contacto',
            name='pedido',
            field=models.ManyToManyField(blank=True, to='aplicacionobmex.Pedido'),
        ),
        migrations.AddField(
            model_name='contacto',
            name='telefono',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacionobmex.Telefono'),
        ),
        migrations.AddField(
            model_name='curso',
            name='direccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacionobmex.Direccion'),
        ),
        migrations.AddField(
            model_name='curso',
            name='participantes',
            field=models.ManyToManyField(blank=True, to='aplicacionobmex.Contacto'),
        ),
        migrations.AddField(
            model_name='institucion',
            name='contacto',
            field=models.ManyToManyField(blank=True, to='aplicacionobmex.Contacto'),
        ),
        migrations.AddField(
            model_name='institucion',
            name='direccion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacionobmex.Direccion'),
        ),
        migrations.AddField(
            model_name='institucion',
            name='pedido',
            field=models.ManyToManyField(blank=True, to='aplicacionobmex.Pedido'),
        ),
        migrations.AddField(
            model_name='institucion',
            name='telefono',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='aplicacionobmex.Telefono'),
        ),
        migrations.AlterField(
            model_name='telefono',
            name='id_Telefono',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
