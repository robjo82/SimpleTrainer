# Generated by Django 2.1.5 on 2019-07-01 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheque', '0005_operatingsytem'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operatingsytem',
            old_name='MacOs',
            new_name='MacO',
        ),
    ]
