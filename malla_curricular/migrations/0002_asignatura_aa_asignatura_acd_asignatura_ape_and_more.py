# Generated by Django 5.0.6 on 2024-05-28 13:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('malla_curricular', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignatura',
            name='aa',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asignatura',
            name='acd',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asignatura',
            name='ape',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asignatura',
            name='pp',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ciclo',
            name='carrera',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='malla_curricular.carrera'),
            preserve_default=False,
        ),
    ]
