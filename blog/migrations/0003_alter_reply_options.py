# Generated by Django 3.2.6 on 2021-08-16 09:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment_reply'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reply',
            options={'verbose_name_plural': 'Replies'},
        ),
    ]