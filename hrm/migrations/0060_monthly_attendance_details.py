# Generated by Django 3.2.9 on 2022-06-08 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0059_alter_leave_application_list_reason'),
    ]

    operations = [
        migrations.CreateModel(
            name='MONTHLY_ATTENDANCE_DETAILS',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('EMP_CODE', models.CharField(default='', max_length=120)),
                ('EMP_NAME', models.CharField(default='', max_length=150)),
                ('DESIGNATION', models.CharField(default='', max_length=150)),
                ('TOTAL_PRESENT', models.CharField(default='', max_length=150)),
                ('TOTAL_ABSENT', models.CharField(default='', max_length=150)),
                ('TIMESTAMP', models.DateTimeField(auto_now_add=True, max_length=50)),
            ],
            options={
                'db_table': 'monthly_attendance_details',
            },
        ),
    ]
