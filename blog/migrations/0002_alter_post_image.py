# Generated by Django 3.2.6 on 2021-08-09 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='pics'),
        ),
    ]