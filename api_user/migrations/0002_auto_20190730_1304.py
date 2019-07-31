# Generated by Django 2.2.3 on 2019-07-30 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=False, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_admin',
            field=models.BooleanField(default=False, help_text='Designates whether this user should assign tasksIn ParentMode is const (api.models.parent_mode = True); in StudentMode changing periodically', verbose_name='is admin'),
        ),
    ]
