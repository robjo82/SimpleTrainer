# Generated by Django 2.1.5 on 2019-04-30 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('EspacePerso', '0003_auto_20190320_1715'),
        ('bibliotheque', '0002_auto_20190425_0835'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stat',
            name='avarage_rating',
        ),
        migrations.RemoveField(
            model_name='stat',
            name='favorite_number',
        ),
        migrations.AddField(
            model_name='stat',
            name='app_functionnality',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='stat',
            name='ease_of_setting_up_the_app',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='stat',
            name='other_comment_on_the_app',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='stat',
            name='other_comment_on_the_site',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='stat',
            name='other_message',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='stat',
            name='overall_app_note',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='stat',
            name='overall_site_note',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='stat',
            name='site_accessibility',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='stat',
            name='site_usefulness',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='stat',
            name='understand_of_record',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='stat',
            name='user_ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EspacePerso.Profil', null=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stat',
            name='utility_of_record',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='stat',
            name='what_functionality_would_you_like_on_the_app',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='stat',
            name='what_functionality_would_you_like_on_the_site',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='stat',
            name='program_ref',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bibliotheque.Program'),
        ),
    ]
