# Generated by Django 2.1.5 on 2019-07-08 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheque', '0014_auto_20190707_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='operating_system_ref',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='bibliotheque.OperatingSystem'),
        ),
        migrations.AlterField(
            model_name='program',
            name='stat_ref',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='bibliotheque.Stat'),
        ),
    ]
