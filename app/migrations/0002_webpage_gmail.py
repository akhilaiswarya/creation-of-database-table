# Generated by Django 4.2.7 on 2023-12-13 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='webpage',
            name='gmail',
            field=models.EmailField(default='https://india.com', max_length=254),
        ),
    ]
