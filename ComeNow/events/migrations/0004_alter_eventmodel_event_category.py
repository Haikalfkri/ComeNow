# Generated by Django 5.0.6 on 2024-06-11 02:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("events", "0003_rename_catogory_eventcategories_category"),
    ]

    operations = [
        migrations.AlterField(
            model_name="eventmodel",
            name="event_category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="events.eventcategories"
            ),
        ),
    ]