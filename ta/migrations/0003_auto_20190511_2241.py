# Generated by Django 2.1.7 on 2019-05-11 22:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ta', '0002_ta_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ta',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
