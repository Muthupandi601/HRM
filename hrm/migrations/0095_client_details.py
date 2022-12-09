# Generated by Django 3.2.9 on 2022-08-04 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0094_client_list_unit_list'),
    ]

    operations = [
        migrations.CreateModel(
            name='CLIENT_DETAILS',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('CLIENT', models.CharField(max_length=200)),
                ('COUNTRY_NAME', models.CharField(max_length=200)),
                ('STATE_NAME', models.CharField(default='', max_length=200)),
                ('DISTRICT_NAME', models.CharField(default='', max_length=200)),
                ('BRANCH_NAME', models.CharField(default='', max_length=200)),
                ('AREA_NAME', models.CharField(default='', max_length=200)),
                ('UNIT', models.CharField(default='', max_length=200)),
            ],
            options={
                'db_table': 'client_details',
            },
        ),
    ]