# Generated by Django 3.2.6 on 2021-08-30 20:38

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=20, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
                'db_table': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'comments',
            },
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(help_text='We will use this email to reach out to you.', max_length=254, verbose_name='email address')),
                ('username', models.CharField(blank=True, max_length=20)),
                ('message', models.TextField(help_text='Please provide your query here.')),
                ('date_sent', models.DateTimeField(default=django.utils.timezone.now)),
                ('is_urgent', models.BooleanField(default=False, help_text='Designates whether the request is URGENT.', verbose_name='urgent status')),
            ],
            options={
                'verbose_name_plural': 'Contact Us',
                'db_table': 'contact_us',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=120, unique=True)),
                ('content', ckeditor.fields.RichTextField()),
                ('snippet', models.TextField()),
                ('image', models.ImageField(default='default.jpg', upload_to='pics')),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
                ('last_modifed', models.DateTimeField(auto_now=True)),
                ('is_pinned', models.BooleanField(default=False, help_text='Designates whether the post is pinned', verbose_name='pinned status')),
            ],
            options={
                'db_table': 'posts',
                'ordering': ['-is_pinned', '-date_posted'],
            },
        ),
        migrations.CreateModel(
            name='PostCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'post_category',
            },
        ),
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('entity', models.CharField(max_length=20, verbose_name='Type')),
                ('url', models.URLField()),
                ('message', ckeditor.fields.RichTextField(blank=True, help_text='If you want to leave a note for the reviewer')),
                ('date_reported', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'db_table': 'reports',
            },
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('reply', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='blog.comment')),
            ],
            options={
                'verbose_name_plural': 'Replies',
                'db_table': 'replies',
            },
        ),
    ]
