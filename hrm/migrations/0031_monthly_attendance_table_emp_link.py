# Generated by Django 3.2.9 on 2022-04-13 08:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0030_salary_details_net_pay'),
    ]

    operations = [
        migrations.AddField(
            model_name='monthly_attendance_table',
            name='EMP_LINK',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='hrm.salary_details', verbose_name='emp_link'),
        ),
    ]
