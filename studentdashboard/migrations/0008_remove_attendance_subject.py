# Generated by Django 2.2.7 on 2020-03-31 06:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('studentdashboard', '0007_auto_20200330_1956'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='attendance',
            name='subject',
        ),
    ]