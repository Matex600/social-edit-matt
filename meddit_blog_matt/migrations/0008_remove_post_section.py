# Generated by Django 3.2 on 2022-02-15 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meddit_blog_matt', '0007_alter_category_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='section',
        ),
    ]