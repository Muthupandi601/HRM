# Generated by Django 3.2.9 on 2022-07-19 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0093_rename_state_code_state_list_state_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='CLIENT_LIST',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('CLIENT', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'client_list',
            },
        ),
        migrations.CreateModel(
            name='UNIT_LIST',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('UNIT_ID', models.CharField(default='', max_length=50)),
                ('UNIT', models.CharField(default='', max_length=200)),
                ('CLIENT', models.CharField(default='', max_length=200)),
            ],
            options={
                'db_table': 'unit_list',
            },
        ),
    ]
