# Generated by Django 3.0.4 on 2020-12-27 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='upload/images/')),
                ('phone', models.IntegerField()),
                ('Email', models.EmailField(max_length=254)),
                ('bio', models.CharField(max_length=200)),
            ],
        ),
    ]