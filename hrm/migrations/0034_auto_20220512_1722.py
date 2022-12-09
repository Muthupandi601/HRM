# Generated by Django 3.2.9 on 2022-05-12 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0033_new_customer_reg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new_customer_reg',
            name='ADDRESS',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='new_customer_reg',
            name='CLIENT_TYPE',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='new_customer_reg',
            name='CONTACT_NO',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='new_customer_reg',
            name='DOB',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='new_customer_reg',
            name='EMAIL',
            field=models.CharField(default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='new_customer_reg',
            name='EMERGENCY_CONTACT_NO',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterModelTable(
            name='new_customer_reg',
            table='customer_register',
        ),
    ]
