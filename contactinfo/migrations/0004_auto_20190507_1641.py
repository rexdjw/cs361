# Generated by Django 2.1.7 on 2019-05-07 16:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contactinfo', '0003_auto_20190408_0404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactinfo',
            name='account',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]