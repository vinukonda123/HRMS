# Generated by Django 4.2.3 on 2023-12-15 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0019_delete_rbi_data_import'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rbi_Data_Import',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank', models.CharField(max_length=100)),
                ('ifsc', models.CharField(max_length=100)),
                ('branch', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city1', models.CharField(max_length=100)),
                ('city2', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('std_code', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=100)),
            ],
        ),
    ]