# Generated by Django 5.1.1 on 2024-09-24 20:57

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="note",
            old_name="created_time",
            new_name="created_at",
        ),
    ]
