# Generated by Django 2.1.5 on 2019-07-07 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheque', '0013_auto_20190704_2024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stat',
            name='operating_system_ref',
        ),
        migrations.RemoveField(
            model_name='stat',
            name='url',
        ),
        migrations.RemoveField(
            model_name='stat',
            name='views_number',
        ),
        migrations.AddField(
            model_name='program',
            name='stat_ref',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bibliotheque.Stat'),
        ),
    ]
