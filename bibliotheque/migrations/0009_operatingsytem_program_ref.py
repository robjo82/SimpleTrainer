# Generated by Django 2.1.5 on 2019-07-02 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheque', '0008_auto_20190701_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='operatingsytem',
            name='program_ref',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bibliotheque.Program'),
        ),
    ]
