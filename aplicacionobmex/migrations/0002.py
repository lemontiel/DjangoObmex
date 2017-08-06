# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-06 03:43
from __future__ import unicode_literals
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

	dependencies = [
	('aplicacionobmex', '0001_initial'),
	]

	operations = [
	migrations.CreateModel(
           name='Pedido',
           fields=[
               ('id_Pedido', models.AutoField(primary_key=True, serialize=False)),
               ('fecha', models.DateTimeField(auto_now=True)),
               ('hora', models.TimeField(auto_now=True)),
               ('cantidad', models.IntegerField(default=0)),
               ('monto', models.FloatField()),
               ('contacto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacionobmex.Contacto')),
               ('institucion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacionobmex.Institucion')),
               ('tipoSilla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aplicacionobmex.Inventario')),
           ],
       )
	]
