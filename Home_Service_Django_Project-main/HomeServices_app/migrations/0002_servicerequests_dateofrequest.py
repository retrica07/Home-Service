# Generated by Django 4.2.4 on 2023-09-06 12:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('HomeServices_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequests',
            name='dateofrequest',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
