# Generated by Django 3.2.3 on 2021-05-21 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0009_auto_20210521_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='actor',
            name='films',
            field=models.ManyToManyField(related_name='films', to='Api.Film'),
        ),
        migrations.AlterField(
            model_name='extrainfo',
            name='genre',
            field=models.IntegerField(choices=[(3, 'Drama'), (0, 'Undefined'), (4, 'Comedy'), (1, 'Horror'), (2, 'Sci=fi')], default=0),
        ),
    ]
