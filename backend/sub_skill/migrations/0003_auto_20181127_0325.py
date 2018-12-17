# Generated by Django 2.0.5 on 2018-11-27 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sub_skill', '0002_auto_20181121_1748'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subskill',
            options={'managed': True, 'ordering': ('skill', 'priority', 'name')},
        ),
        migrations.AddField(
            model_name='subskill',
            name='priority',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]