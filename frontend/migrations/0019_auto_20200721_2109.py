# Generated by Django 2.2.7 on 2020-07-21 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0018_eventdetail_videourl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdetail',
            name='videourl',
            field=models.TextField(default='', max_length=500),
        ),
    ]
