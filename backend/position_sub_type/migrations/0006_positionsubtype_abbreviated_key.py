# Generated by Django 2.0.5 on 2019-02-07 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('position_sub_type', '0005_positionsubtype_select_option_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='positionsubtype',
            name='abbreviated_key',
            field=models.CharField(blank=True, max_length=1),
        ),
    ]
