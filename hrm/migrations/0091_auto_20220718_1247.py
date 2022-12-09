# Generated by Django 3.2.9 on 2022-07-18 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0090_city_list_country_list_state_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='city_list',
            name='CITY_ID',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='state_list',
            name='STATE_ID',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='city_list',
            name='CITY_NAME',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='city_list',
            name='COUNTRY_NAME',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='city_list',
            name='STATE_NAME',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='state_list',
            name='COUNTRY_NAME',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='state_list',
            name='STATE_NAME',
            field=models.CharField(default='', max_length=200),
        ),
    ]
