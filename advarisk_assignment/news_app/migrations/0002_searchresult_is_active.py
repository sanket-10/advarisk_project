# Generated by Django 3.2 on 2023-10-01 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='searchresult',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
