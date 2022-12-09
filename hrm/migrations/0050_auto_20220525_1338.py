# Generated by Django 3.2.9 on 2022-05-25 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0049_emp_daily_attendance'),
    ]

    operations = [
        migrations.CreateModel(
            name='EMP_DAILY_ATTENDANCE_LIST',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('EMP_CODE', models.CharField(default='', max_length=120)),
                ('EMP_NAME', models.CharField(default='', max_length=150)),
                ('DESIGNATION', models.CharField(default='', max_length=150)),
                ('IN_TIME', models.CharField(default='', max_length=100)),
                ('OUT_TIME', models.CharField(default='', max_length=100)),
                ('LEAVE_CATEGORY', models.CharField(default='', max_length=200)),
                ('ATTENDANCE_DATE', models.CharField(default='', max_length=100)),
                ('TIMESTAMP', models.DateTimeField(auto_now_add=True, max_length=50)),
            ],
            options={
                'db_table': 'emp_daily_attendance_list',
            },
        ),
        migrations.RenameModel(
            old_name='EMP_DAILY_ATTENDANCE',
            new_name='EMP_DAILY_ATTENDANCE_UPDATED',
        ),
        migrations.AlterModelTable(
            name='emp_daily_attendance_updated',
            table='emp_daily_attendance_updated',
        ),
    ]
