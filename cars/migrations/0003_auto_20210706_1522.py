# Generated by Django 3.1.7 on 2021-07-06 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0002_auto_20210706_1514'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='engine',
            new_name='engine_capacity',
        ),
    ]
