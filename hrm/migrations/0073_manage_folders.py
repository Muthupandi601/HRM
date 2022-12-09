# Generated by Django 3.2.9 on 2022-06-27 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0072_alter_notice_board_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='MANAGE_FOLDERS',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('FOLDER_NAME', models.CharField(default='', max_length=120)),
                ('DESCRIPTION', models.CharField(default='', max_length=600)),
                ('CREATED_AT', models.CharField(default='', max_length=150)),
                ('TIMESTAMP', models.DateTimeField(auto_now_add=True, max_length=50)),
            ],
            options={
                'db_table': 'manage_folder',
            },
        ),
    ]
