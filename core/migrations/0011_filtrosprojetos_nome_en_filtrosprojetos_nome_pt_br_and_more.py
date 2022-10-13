# Generated by Django 4.1.1 on 2022-10-13 21:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_competencia_competencia_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='filtrosprojetos',
            name='nome_en',
            field=models.CharField(max_length=30, null=True, verbose_name='Nome_filtro'),
        ),
        migrations.AddField(
            model_name='filtrosprojetos',
            name='nome_pt_br',
            field=models.CharField(max_length=30, null=True, verbose_name='Nome_filtro'),
        ),
        migrations.AddField(
            model_name='projetos',
            name='nome_en',
            field=models.CharField(max_length=50, null=True, verbose_name='Nome'),
        ),
        migrations.AddField(
            model_name='projetos',
            name='nome_pt_br',
            field=models.CharField(max_length=50, null=True, verbose_name='Nome'),
        ),
    ]
