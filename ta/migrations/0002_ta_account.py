# Generated by Django 2.1.7 on 2019-04-07 20:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ta',
            name='account',
            field=models.ForeignKey(default=123, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
