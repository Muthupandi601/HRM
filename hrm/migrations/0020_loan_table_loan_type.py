# Generated by Django 3.2.8 on 2022-02-26 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0019_loan_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='loan_table',
            name='LOAN_TYPE',
            field=models.CharField(default='', max_length=25),
        ),
    ]
