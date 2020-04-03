# Generated by Django 2.2.7 on 2020-04-03 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacherdashboard', '0004_teachers_username'),
        ('studentdashboard', '0011_marks_remarks'),
    ]

    operations = [
        migrations.AddField(
            model_name='marks',
            name='marked_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='teacherdashboard.teachers'),
            preserve_default=False,
        ),
    ]