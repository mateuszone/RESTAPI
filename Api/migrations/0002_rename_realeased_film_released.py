# Generated by Django 3.2.3 on 2021-05-19 22:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='film',
            old_name='realeased',
            new_name='released',
        ),
    ]