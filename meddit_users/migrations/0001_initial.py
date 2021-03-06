# Generated by Django 3.2 on 2022-02-24 20:01

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_bio', models.TextField()),
                ('user_image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('github_url', models.CharField(blank=True, max_length=225, null=True)),
                ('linkedin_url', models.CharField(blank=True, max_length=225, null=True)),
                ('facebook_url', models.CharField(blank=True, max_length=225, null=True)),
                ('twitter_url', models.CharField(blank=True, max_length=225, null=True)),
                ('instagram_url', models.CharField(blank=True, max_length=225, null=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
