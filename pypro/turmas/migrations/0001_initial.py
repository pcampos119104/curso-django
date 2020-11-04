# Generated by Django 3.1.2 on 2020-10-28 11:36

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Turma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=64)),
                ('slug', models.SlugField(max_length=64)),
                ('inicio', models.DateField()),
                ('fim', models.DateField()),
            ],
        ),
    ]
