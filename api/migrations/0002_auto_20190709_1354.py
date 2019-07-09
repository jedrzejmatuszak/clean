# Generated by Django 2.2.3 on 2019-07-09 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='room',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='roommate',
        ),
        migrations.RemoveField(
            model_name='record',
            name='roommate',
        ),
        migrations.RemoveField(
            model_name='room',
            name='clean',
        ),
        migrations.AddField(
            model_name='clean',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Room'),
        ),
        migrations.AddField(
            model_name='record',
            name='date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='record',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Room'),
        ),
        migrations.AddField(
            model_name='room',
            name='flat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Flat'),
        ),
        migrations.AlterField(
            model_name='record',
            name='clean',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Clean'),
        ),
        migrations.AlterField(
            model_name='record',
            name='flat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Flat'),
        ),
        migrations.CreateModel(
            name='Flatmate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Flat')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='record',
            name='flatmate',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.Flatmate'),
        ),
    ]
