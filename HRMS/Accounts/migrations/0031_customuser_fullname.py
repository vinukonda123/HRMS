# Generated by Django 4.2.3 on 2023-12-26 07:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0030_financial_year_financial_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='fullname',
            field=models.CharField(default=True, max_length=100),
            preserve_default=False,
        ),
    ]
