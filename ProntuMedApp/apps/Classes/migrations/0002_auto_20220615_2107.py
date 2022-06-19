# Generated by Django 3.2.5 on 2022-06-16 00:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='enfermeiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=155)),
                ('celular', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='Paciente_prontuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(max_length=11)),
                ('nome', models.CharField(max_length=200)),
                ('celular', models.CharField(max_length=12)),
            ],
        ),
        migrations.DeleteModel(
            name='Medico',
        ),
        migrations.DeleteModel(
            name='Paciente',
        ),
    ]
