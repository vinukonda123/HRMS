# Generated by Django 4.2.3 on 2023-12-12 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0008_tickets'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tickets',
            name='employee',
        ),
    ]
