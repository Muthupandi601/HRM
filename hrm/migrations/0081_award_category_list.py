# Generated by Django 3.2.9 on 2022-07-02 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0080_client_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='AWARD_CATEGORY_LIST',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('AWARD_CATEGORY', models.CharField(default='', max_length=120)),
                ('CREATED_AT', models.CharField(default='', max_length=150)),
                ('STATUS', models.CharField(default='', max_length=150)),
                ('TIMESTAMP', models.DateTimeField(auto_now_add=True, max_length=50)),
            ],
            options={
                'db_table': 'award_category_list',
            },
        ),
    ]
