# Generated by Django 3.2.6 on 2021-08-25 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_customuser_telephone'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_librarian',
            field=models.BooleanField(default=False, help_text='Designates whether the user can edit the book store database.', verbose_name='librarian status'),
        ),
    ]
