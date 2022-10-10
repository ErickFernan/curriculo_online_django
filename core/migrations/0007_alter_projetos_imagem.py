# Generated by Django 4.1.1 on 2022-10-05 20:19

import core.models
from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_filtrosprojetos_skill_projetos'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projetos',
            name='imagem',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 300, 'width': 400}}, verbose_name='Imagem'),
        ),
    ]