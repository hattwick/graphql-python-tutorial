# Generated by Django 2.0.2 on 2018-10-08 05:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0008_auto_20181008_0502'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='story',
            name='date_published',
        ),
    ]
