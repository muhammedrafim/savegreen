# Generated by Django 2.2.7 on 2020-03-25 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0010_auto_20200325_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventsnews',
            name='eventtype',
            field=models.TextField(choices=[('SPORTS', 'Sports'), ('ADMISSION', 'Admission'), ('ACADEMIC', 'Academic')]),
        ),
    ]
