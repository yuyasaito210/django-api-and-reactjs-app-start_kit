# Generated by Django 2.0.2 on 2018-07-24 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talent_picture', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='talentpicture',
            name='url',
            field=models.TextField(blank=True, null=True),
        ),
    ]
