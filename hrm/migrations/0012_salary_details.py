# Generated by Django 3.2.8 on 2022-02-08 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0011_auto_20220202_1517'),
    ]

    operations = [
        migrations.CreateModel(
            name='salary_details',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('EMP_CODE', models.CharField(max_length=50)),
                ('FIXED_SALARY', models.IntegerField(default=0)),
                ('BASIC', models.IntegerField(default=0)),
                ('DEARANCE_ALLOWANCES', models.IntegerField(default=0)),
                ('SPECIAL_ALLOWANCES', models.IntegerField(default=0)),
                ('HOUSE_RENT_ALLOWANCES', models.IntegerField(default=0)),
                ('CONVEYANCE', models.IntegerField(default=0)),
                ('OTHER_ALLOWANCES', models.IntegerField(default=0)),
                ('OVERTIME_AMOUNT', models.IntegerField(default=0)),
                ('SITE_ALLOWANCES', models.IntegerField(default=0)),
                ('SHIFT_ALLOWANCES_AMOUNT', models.IntegerField(default=0)),
                ('INCENTIVE', models.IntegerField(default=0)),
                ('LEAVE_TRAVEL_ALLOWANCES', models.IntegerField(default=0)),
                ('MEDICAL_ALLOWANCES', models.IntegerField(default=0)),
                ('CHILD_EDUCATIONS_ALLOWANCES', models.IntegerField(default=0)),
                ('ATTENDANCE_BONUS', models.IntegerField(default=0)),
                ('ATTENDANCE_INCENTIVE', models.IntegerField(default=0)),
                ('MONTHLY_BOUNS', models.IntegerField(default=0)),
                ('MONTHLY_LEAVE_WAGES', models.IntegerField(default=0)),
                ('RELIVER_DUTY_WAGES', models.IntegerField(default=0)),
                ('ARREARS_WAGES', models.IntegerField(default=0)),
                ('PROFESSIONAL_TAX', models.IntegerField(default=0)),
                ('LABOUR_WELFARE_FUND', models.IntegerField(default=0)),
                ('INCOME_TAX', models.IntegerField(default=0)),
                ('LOAN', models.IntegerField(default=0)),
                ('SALARY_ADVANCE', models.IntegerField(default=0)),
                ('OTHER_DEDUCTION', models.IntegerField(default=0)),
                ('UNIFORM_DEDUCTION', models.IntegerField(default=0)),
                ('TIMESTAMP', models.DateTimeField(auto_now_add=True, max_length=50)),
            ],
            options={
                'db_table': 'emp_salary_details',
            },
        ),
    ]