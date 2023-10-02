# Generated by Django 3.2 on 2023-10-01 07:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('news_app', '0002_searchresult_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='keyword',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2023, 10, 1, 7, 21, 58, 873257, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='keyword',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='keyword',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='searchresult',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='searchresult',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
