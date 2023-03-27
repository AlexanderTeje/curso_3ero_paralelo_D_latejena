# Generated by Django 4.1.7 on 2023-03-27 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='usuario',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('usuario', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=60)),
                ('estado', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'usuario',
            },
        ),
        migrations.CreateModel(
            name='informacion',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('ci', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('fcha_nacimiento', models.DateField()),
                ('direccion', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iniciosesion.usuario')),
            ],
            options={
                'db_table': 'informacion',
            },
        ),
    ]
