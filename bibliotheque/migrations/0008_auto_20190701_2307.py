# Generated by Django 2.1.5 on 2019-07-01 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheque', '0007_auto_20190701_2300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operatingsytem',
            old_name='Windows',
            new_name='OldVersionsWindows',
        ),
        migrations.AddField(
            model_name='operatingsytem',
            name='Windows10',
            field=models.BooleanField(default=True),
        ),
    ]
