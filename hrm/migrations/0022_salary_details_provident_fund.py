# Generated by Django 3.2.9 on 2022-04-02 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0021_auto_20220227_1606'),
    ]

    operations = [
        migrations.AddField(
            model_name='salary_details',
            name='PROVIDENT_FUND',
            field=models.CharField(default='', max_length=150),
        ),
    ]
