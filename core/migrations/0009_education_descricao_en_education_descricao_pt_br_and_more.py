# Generated by Django 4.1.1 on 2022-10-13 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_remove_projetos_tag_projetos_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='descricao_en',
            field=models.TextField(max_length=200, null=True, verbose_name='Descrição'),
        ),
        migrations.AddField(
            model_name='education',
            name='descricao_pt_br',
            field=models.TextField(max_length=200, null=True, verbose_name='Descrição'),
        ),
        migrations.AddField(
            model_name='education',
            name='subtitulo_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Subtítulo'),
        ),
        migrations.AddField(
            model_name='education',
            name='subtitulo_pt_br',
            field=models.CharField(max_length=100, null=True, verbose_name='Subtítulo'),
        ),
        migrations.AddField(
            model_name='education',
            name='titulo_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Título'),
        ),
        migrations.AddField(
            model_name='education',
            name='titulo_pt_br',
            field=models.CharField(max_length=100, null=True, verbose_name='Título'),
        ),
    ]