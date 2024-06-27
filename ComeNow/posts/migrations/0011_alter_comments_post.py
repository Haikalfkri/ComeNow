# Generated by Django 5.0.6 on 2024-06-26 08:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0010_rename_posts_comments_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comments",
            name="post",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="posts_comment",
                to="posts.posts",
            ),
        ),
    ]