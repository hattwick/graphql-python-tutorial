# Generated by Django 2.2 on 2019-04-16 03:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0011_auto_20190408_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='passage',
            name='pov_character',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='in_passages', to='story.Character'),
        ),
    ]
