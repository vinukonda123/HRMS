# Generated by Django 4.2.3 on 2023-12-18 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0023_holidays_excel'),
    ]

    operations = [
        migrations.AddField(
            model_name='bank_account',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]