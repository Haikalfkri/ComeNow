# Generated by Django 5.0.6 on 2024-06-03 03:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentication", "0003_remove_userprofile_fullname_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="phone_number",
            field=models.IntegerField(blank=True, max_length=12),
        ),
    ]
