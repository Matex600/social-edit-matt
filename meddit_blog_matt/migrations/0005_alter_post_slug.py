# Generated by Django 3.2 on 2022-02-13 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meddit_blog_matt', '0004_auto_20220213_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=models.SlugField(max_length=300, null=True, unique=True),
        ),
    ]
