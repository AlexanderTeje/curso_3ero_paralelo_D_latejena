# Generated by Django 4.1.7 on 2023-03-27 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='duenomascota',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'duenomascota',
            },
        ),
        migrations.CreateModel(
            name='animal',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion_consulta', models.TextField()),
                ('estado', models.BooleanField(default=True)),
                ('dueno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='veterinaria.duenomascota')),
            ],
            options={
                'db_table': 'animal',
            },
        ),
    ]
