# Generated by Django 3.2.3 on 2021-05-21 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0008_auto_20210521_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='genre',
            field=models.IntegerField(choices=[(4, 'Comedy'), (0, 'Undefined'), (2, 'Sci=fi'), (3, 'Drama'), (1, 'Horror')], default=0),
        ),
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
                ('films', models.ManyToManyField(to='Api.Film')),
            ],
        ),
    ]