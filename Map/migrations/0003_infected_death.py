# Generated by Django 3.0.3 on 2020-04-13 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Map', '0002_auto_20200412_0827'),
    ]

    operations = [
        migrations.AddField(
            model_name='infected',
            name='death',
            field=models.IntegerField(default=0),
        ),
    ]
