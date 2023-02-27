# Generated by Django 4.1.1 on 2023-02-27 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0011_filtrosprojetos_nome_en_filtrosprojetos_nome_pt_br_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='descricao',
            field=models.TextField(max_length=300, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='descricao_en',
            field=models.TextField(max_length=300, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='descricao_pt_br',
            field=models.TextField(max_length=300, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='service',
            name='icone',
            field=models.CharField(choices=[('fa fa-2x fa-laptop service-icon bg-primary text-white mr-3', 'Laptop'), ('fa fa-2x fa-laptop-code service-icon bg-primary text-white mr-3', 'Laptop-code'), ('fab fa-2x fa-android service-icon bg-primary text-white mr-3', 'Android'), ('fab fa-2x fa-apple service-icon bg-primary text-white mr-3', 'Apple'), ('fa fa-2x fa-search service-icon bg-primary text-white mr-3', 'Search'), ('fa fa-2x fa-edit service-icon bg-primary text-white mr-3', 'Edit'), ('fa fa-2x fa-solid fa-robot service-icon bg-primary text-white mr-3', 'Robot'), ('fa fa-2x fa-solid fa-bolt service-icon bg-primary text-white mr-3', 'Lightning'), ('fa fa-2x fa-cog service-icon bg-primary text-white mr-3', 'Gear')], max_length=100, verbose_name='Icone'),
        ),
        migrations.AlterField(
            model_name='sobre',
            name='descricao',
            field=models.TextField(max_length=400, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='sobre',
            name='descricao_en',
            field=models.TextField(max_length=400, null=True, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='sobre',
            name='descricao_pt_br',
            field=models.TextField(max_length=400, null=True, verbose_name='Descrição'),
        ),
    ]
