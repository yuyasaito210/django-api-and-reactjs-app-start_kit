# Generated by Django 2.0.5 on 2018-12-10 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('position_type', '0006_positiontype_select_option_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='positiontype',
            name='introduction_link',
            field=models.CharField(blank=True, max_length=1024),
        ),
    ]