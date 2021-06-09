# Generated by Django 3.2.3 on 2021-05-21 12:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0007_auto_20210521_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='genre',
            field=models.IntegerField(choices=[(3, 'Drama'), (2, 'Sci=fi'), (0, 'Undefined'), (1, 'Horror'), (4, 'Comedy')], default=0),
        ),
        migrations.AlterField(
            model_name='review',
            name='film',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review', to='Api.film'),
        ),
    ]