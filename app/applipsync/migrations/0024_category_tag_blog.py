# Generated by Django 4.1.3 on 2023-02-04 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applipsync', '0023_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('body', models.TextField()),
                ('image', models.ImageField(upload_to='images/blog_images/')),
                ('categories', models.ManyToManyField(to='applipsync.category')),
                ('tags', models.ManyToManyField(to='applipsync.tag')),
            ],
        ),
    ]
