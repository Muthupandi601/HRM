# Generated by Django 3.2.9 on 2022-06-15 11:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hrm', '0066_leave_category_list_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leave_category_list',
            name='IMAGE',
        ),
    ]