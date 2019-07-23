# Generated by Django 2.2.3 on 2019-07-23 16:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Otp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.IntegerField(unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='fathers_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='myuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='myuser',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
        ),
        migrations.AddField(
            model_name='myuser',
            name='last_name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='myuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10, validators=[django.core.validators.RegexValidator(message='Phone', regex='^\\+?1?\\d{9,15}$')]),
        ),
        migrations.AddField(
            model_name='myuser',
            name='spouse_name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
