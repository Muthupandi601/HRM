# Generated by Django 3.2.9 on 2022-07-07 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0084_personal_event'),
    ]

    operations = [
        migrations.CreateModel(
            name='ATTENDANCE_SETTING',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('ATTENDANCE_SETTING', models.CharField(default='', max_length=120)),
                ('TIMESTAMP', models.DateTimeField(auto_now_add=True, max_length=50)),
            ],
            options={
                'db_table': 'attendance_setting',
            },
        ),
    ]
