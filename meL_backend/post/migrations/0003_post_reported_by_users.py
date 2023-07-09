# Generated by Django 4.2.3 on 2023-07-08 11:43

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0002_post_is_private'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reported_by_users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]