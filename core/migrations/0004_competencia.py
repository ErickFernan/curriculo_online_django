# Generated by Django 4.1.1 on 2022-09-29 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_sobre_escolaridade_alter_sobre_nome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Competencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criado')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualizado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('competencia', models.CharField(max_length=40, verbose_name='Competência')),
            ],
            options={
                'verbose_name': 'Competência',
                'verbose_name_plural': 'Competências',
            },
        ),
    ]
