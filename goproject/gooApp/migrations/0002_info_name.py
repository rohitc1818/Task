# Generated by Django 3.0.4 on 2020-12-28 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gooApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='info',
            name='name',
            field=models.CharField(default='', max_length=20),
        ),
    ]
