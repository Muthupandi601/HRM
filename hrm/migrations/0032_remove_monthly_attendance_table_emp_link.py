# Generated by Django 3.2.9 on 2022-04-13 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0031_monthly_attendance_table_emp_link'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='monthly_attendance_table',
            name='EMP_LINK',
        ),
    ]
