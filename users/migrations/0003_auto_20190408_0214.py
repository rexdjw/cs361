# Generated by Django 2.1.7 on 2019-04-08 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contactinfo', '0002_contactinfo_account'),
        ('users', '0002_usergroup_contact_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usergroup',
            name='contact_info',
        ),
        migrations.AddField(
            model_name='users',
            name='contact_info',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='contactinfo.ContactInfo'),
        ),
    ]
