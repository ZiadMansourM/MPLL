# Generated by Django 3.2.6 on 2021-08-24 13:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20210824_1546'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='postcategory',
            table='post_category',
        ),
        migrations.AlterModelTable(
            name='report',
            table='reports',
        ),
    ]