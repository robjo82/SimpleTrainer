# Generated by Django 2.1.5 on 2019-07-02 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheque', '0009_operatingsytem_program_ref'),
    ]

    operations = [
        migrations.AddField(
            model_name='operatingsytem',
            name='operating_system_ref',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bibliotheque.Stat'),
        ),
    ]
