# Generated by Django 5.1.3 on 2024-11-24 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("herro", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="exercice",
            old_name="thumbnail",
            new_name="Image",
        ),
        migrations.AddField(
            model_name="exercice",
            name="unité",
            field=models.CharField(
                choices=[("kg", "kg"), ("km/h", "km/h"), ("min/km", "min/km")],
                default=("kg", "kg"),
                max_length=10,
            ),
        ),
    ]
