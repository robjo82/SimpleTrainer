# Generated by Django 2.2 on 2019-04-25 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheque', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='program',
            name='slug',
            field=models.SlugField(default='programme_<built-in function id>'),
        ),
        migrations.AddField(
            model_name='program',
            name='youtube_code',
            field=models.TextField(null=True),
        ),
    ]
