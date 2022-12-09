# Generated by Django 3.2.9 on 2022-06-02 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0054_remove_expense_category_list_exp_code'),
    ]

    operations = [
        migrations.CreateModel(
            name='LEAVE_CATEGORY_LIST',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('CATEGORY_NAME', models.CharField(default='', max_length=150)),
                ('CATEGORY_DESCRIPTION', models.CharField(default='', max_length=150)),
                ('STATUS', models.CharField(default='', max_length=150)),
                ('ADDED_DATE', models.CharField(default='', max_length=150)),
                ('TIMESTAMP', models.DateTimeField(auto_now_add=True, max_length=50)),
            ],
            options={
                'db_table': 'leave_category_list',
            },
        ),
    ]