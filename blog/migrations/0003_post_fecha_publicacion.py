# Generated by Django 5.1.2 on 2024-10-16 23:17

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_autor_remove_post_fecha_publicacion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='fecha_publicacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
