# Generated by Django 3.2.6 on 2023-11-03 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0009_auto_20231103_1902'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('emailId', models.CharField(max_length=100)),
            ],
        ),
    ]
