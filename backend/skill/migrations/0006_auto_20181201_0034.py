# Generated by Django 2.0.5 on 2018-12-01 00:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skill', '0005_auto_20181129_0153'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='video_audition_button_title',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='skill',
            name='wizard_button_title',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
