# Generated by Django 5.0.6 on 2024-06-13 00:26

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0008_eventmodel_like_count_remove_eventmodel_likes_and_more"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name="eventmodel",
            name="like_count",
        ),
        migrations.RemoveField(
            model_name="eventmodel",
            name="likes",
        ),
        migrations.AddField(
            model_name="eventmodel",
            name="liked_by",
            field=models.ManyToManyField(
                blank=True, related_name="event_like", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
