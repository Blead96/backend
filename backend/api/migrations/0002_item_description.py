# Generated by Django 4.2.7 on 2023-11-27 10:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("api", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="description",
            field=models.TextField(default="Default description"),
        ),
    ]
