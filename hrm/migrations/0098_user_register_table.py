# Generated by Django 3.2.9 on 2022-08-12 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0097_emp_salary_maintains'),
    ]

    operations = [
        migrations.CreateModel(
            name='USER_REGISTER_TABLE',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('USER_NAME', models.CharField(max_length=50)),
                ('PASSWORD', models.CharField(max_length=300)),
                ('E_MAIL', models.CharField(default='', max_length=125)),
                ('REGISTER_DATE', models.CharField(default='', max_length=150)),
                ('TIMESTAMP', models.DateTimeField(auto_now_add=True, max_length=50)),
            ],
            options={
                'db_table': 'user_register_table',
            },
        ),
    ]