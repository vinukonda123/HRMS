# Generated by Django 4.2.3 on 2023-12-15 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0017_rbi_data'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rbi_Data',
            new_name='Rbi_Data_Import',
        ),
    ]