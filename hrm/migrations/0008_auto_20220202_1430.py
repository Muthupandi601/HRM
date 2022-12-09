# Generated by Django 3.2.8 on 2022-02-02 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0007_admin_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='monthly_attendance',
            old_name='ABSENT',
            new_name='ARREARS_WAGES',
        ),
        migrations.RenameField(
            model_name='monthly_attendance',
            old_name='ADVANCE',
            new_name='ATTENDANCE_BONUS',
        ),
        migrations.RenameField(
            model_name='monthly_attendance',
            old_name='BASIC_RATE',
            new_name='ATTENDANCE_INCENTIVE',
        ),
        migrations.RenameField(
            model_name='monthly_attendance',
            old_name='DAYS_PRESENT',
            new_name='BASIC',
        ),
        migrations.RenameField(
            model_name='monthly_attendance',
            old_name='DIVIDE_BY_DAYS',
            new_name='CHILD_EDUCATIONS_ALLOWANCES',
        ),
        migrations.RenameField(
            model_name='monthly_attendance',
            old_name='EXTRA_DUTIES',
            new_name='CONVEYANCE',
        ),
        migrations.RenameField(
            model_name='monthly_attendance',
            old_name='INVENTORY',
            new_name='DEARANCE_ALLOWANCES',
        ),
        migrations.RenameField(
            model_name='monthly_attendance',
            old_name='OT_HRS',
            new_name='FIXED_SALARY',
        ),
        migrations.RenameField(
            model_name='monthly_attendance',
            old_name='PT',
            new_name='HOUSE_RENT_ALLOWANCES',
        ),
        migrations.RenameField(
            model_name='monthly_attendance',
            old_name='TDS',
            new_name='INCENTIVE',
        ),
        migrations.RenameField(
            model_name='monthly_attendance',
            old_name='TOTAL_DAYS',
            new_name='INCOME_TAX',
        ),
        migrations.RenameField(
            model_name='monthly_attendance',
            old_name='WEEKLY_OFFS',
            new_name='LABOUR_WELFARE_FUND',
        ),
        migrations.RemoveField(
            model_name='monthly_attendance',
            name='OTHER_DEDUCTION_DESCRIPTION',
        ),
        migrations.AddField(
            model_name='monthly_attendance',
            name='LEAVE_TRAVEL_ALLOWANCES',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='monthly_attendance',
            name='LOAN',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='monthly_attendance',
            name='MEDICAL_ALLOWANCES',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='monthly_attendance',
            name='MONTHLY_BOUNS',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='monthly_attendance',
            name='MONTHLY_LEAVE_WAGES',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='monthly_attendance',
            name='PROFESSIONAL_TAX',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='monthly_attendance',
            name='RELIVER_DUTY_WAGES',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='monthly_attendance',
            name='SALARY_ADVANCE',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='monthly_attendance',
            name='SHIFT_ALLOWANCES',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='monthly_attendance',
            name='SITE_ALLOWANCES',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='monthly_attendance',
            name='SPECIAL_ALLOWANCES',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='monthly_attendance',
            name='UNIFORM_DEDUCTION',
            field=models.IntegerField(default=0),
        ),
    ]
