# Generated by Django 3.1.2 on 2020-10-14 11:18

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('modulos', '0003_populando_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modulo',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
