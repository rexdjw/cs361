# Generated by Django 2.1.7 on 2019-04-08 04:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contactinfo', '0002_contactinfo_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='account',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
