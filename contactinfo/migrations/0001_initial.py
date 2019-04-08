# Generated by Django 2.1.7 on 2019-04-07 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('phoneNumber', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=64)),
                ('address', models.CharField(max_length=256)),
                ('officeHours', models.CharField(max_length=32)),
                ('officeNumber', models.CharField(max_length=32)),
            ],
        ),
    ]