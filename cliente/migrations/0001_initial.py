# Generated by Django 4.2.2 on 2023-07-09 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=55)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('rg', models.CharField(max_length=9)),
                ('ativo', models.BooleanField(default=False)),
                ('data_criacao_cliente', models.DateField(auto_now_add=True)),
            ],
        ),
    ]