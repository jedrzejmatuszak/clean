# Generated by Django 2.2.3 on 2019-07-10 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20190709_1411'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Clean',
            new_name='CleanUp',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='clean',
            new_name='cleanup',
        ),
    ]
