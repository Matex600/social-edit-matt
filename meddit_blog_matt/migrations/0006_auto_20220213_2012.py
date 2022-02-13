# Generated by Django 3.2 on 2022-02-13 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meddit_blog_matt', '0005_alter_post_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(default='Uncategorised', max_length=255),
        ),
    ]