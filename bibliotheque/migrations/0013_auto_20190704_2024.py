# Generated by Django 2.1.5 on 2019-07-04 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheque', '0012_auto_20190702_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='stat',
            name='url',
            field=models.URLField(null=True),
        ),
        migrations.AddField(
            model_name='stat',
            name='views_number',
            field=models.IntegerField(default=1),
        ),
    ]
