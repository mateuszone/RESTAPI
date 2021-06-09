# Generated by Django 3.2.3 on 2021-05-21 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0013_alter_extrainfo_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='genre',
            field=models.IntegerField(choices=[(2, 'Sci=fi'), (4, 'Comedy'), (0, 'Undefined'), (1, 'Horror'), (3, 'Drama')], default=0),
        ),
    ]
