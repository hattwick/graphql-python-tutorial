# Generated by Django 2.0.2 on 2018-10-08 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('story', '0007_auto_20180224_2118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('twitter_account', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='story',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='story.Author'),
        ),
    ]
