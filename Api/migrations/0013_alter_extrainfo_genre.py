# Generated by Django 3.2.3 on 2021-05-21 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0012_auto_20210521_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='genre',
            field=models.IntegerField(choices=[(0, 'Undefined'), (1, 'Horror'), (4, 'Comedy'), (2, 'Sci=fi'), (3, 'Drama')], default=0),
        ),
    ]
