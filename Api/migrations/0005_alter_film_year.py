# Generated by Django 3.2.3 on 2021-05-20 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0004_alter_film_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='year',
            field=models.IntegerField(),
        ),
    ]
