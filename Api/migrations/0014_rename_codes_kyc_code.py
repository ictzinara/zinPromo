# Generated by Django 3.2.6 on 2023-11-04 07:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0013_rename_code_kyc_codes'),
    ]

    operations = [
        migrations.RenameField(
            model_name='kyc',
            old_name='codes',
            new_name='code',
        ),
    ]