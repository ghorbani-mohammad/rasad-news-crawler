# Generated by Django 3.0.5 on 2020-04-19 10:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agency', '0003_auto_20200419_0502'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='agency',
            options={'ordering': ['id']},
        ),
    ]
