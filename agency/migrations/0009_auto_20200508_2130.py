# Generated by Django 3.0.5 on 2020-05-08 21:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0008_agency_alexa_global_rank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agency',
            name='alexa_global_rank',
            field=models.IntegerField(default=0),
        ),
    ]