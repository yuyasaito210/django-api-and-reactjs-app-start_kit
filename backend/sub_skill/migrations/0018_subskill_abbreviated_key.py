# Generated by Django 2.0.5 on 2019-02-07 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_skill', '0017_subskill_video_audition_view_content_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='subskill',
            name='abbreviated_key',
            field=models.CharField(blank=True, max_length=1),
        ),
    ]
