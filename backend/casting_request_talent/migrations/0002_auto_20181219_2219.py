# Generated by Django 2.0.5 on 2018-12-19 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('casting_request_talent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='castingrequesttalent',
            name='talents',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='talent_casting_requests', to='talent.Talent'),
        ),
    ]
