# Generated by Django 3.2.6 on 2021-08-23 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_post_dislikes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dislikes',
        ),
    ]