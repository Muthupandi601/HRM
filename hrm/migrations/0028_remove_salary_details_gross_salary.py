# Generated by Django 3.2.9 on 2022-04-08 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0027_auto_20220402_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salary_details',
            name='GROSS_SALARY',
        ),
    ]