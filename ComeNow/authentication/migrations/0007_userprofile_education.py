# Generated by Django 5.0.6 on 2024-06-19 02:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0006_userprofile_follow_userprofile_follow_count"),
    ]

    operations = [
        migrations.AddField(
            model_name="userprofile",
            name="education",
            field=models.CharField(blank=True, max_length=255),
        ),
    ]