# Generated by Django 3.0.5 on 2020-06-18 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0011_auto_20200515_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='agency',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='agencypagestructure',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
