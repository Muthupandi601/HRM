# Generated by Django 3.2.9 on 2022-09-01 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0102_auto_20220901_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='emp_company_details',
            name='COMPANY_ADDRESS',
            field=models.CharField(default='', max_length=200),
        ),
    ]