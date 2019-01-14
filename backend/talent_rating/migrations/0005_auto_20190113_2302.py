# Generated by Django 2.0.5 on 2019-01-13 23:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('talent', '0002_talent_tid'),
        ('client', '0001_initial'),
        ('casting_request_talent', '0005_auto_20181221_0240'),
        ('talent_rating', '0004_talentrating_casting_request_talent'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='talentrating',
            unique_together={('talent', 'client', 'casting_request_talent')},
        ),
    ]
