# Generated by Django 3.0.3 on 2020-04-18 03:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Shop', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='shop',
        ),
    ]
