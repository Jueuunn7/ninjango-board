# Generated by Django 5.1.5 on 2025-02-06 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("board", "0001_initial"),
    ]

    operations = [
        migrations.AddIndex(
            model_name="board",
            index=models.Index(fields=["title"], name="single_index"),
        ),
    ]
