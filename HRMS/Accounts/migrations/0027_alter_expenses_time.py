# Generated by Django 4.2.3 on 2023-12-18 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0026_expenses_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenses',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
