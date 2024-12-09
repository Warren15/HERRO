# Generated by Django 5.1.3 on 2024-11-24 10:32

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("herro", "0002_rename_thumbnail_exercice_image_exercice_unité"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name="exercice",
            old_name="exercice_name",
            new_name="nom",
        ),
        migrations.AlterField(
            model_name="exercice",
            name="unité",
            field=models.CharField(
                choices=[("kg", "kg"), ("km/h", "km/h")],
                default=("kg", "kg"),
                max_length=10,
            ),
        ),
        migrations.CreateModel(
            name="Perf",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("perf_value", models.FloatField(default=0.0)),
                ("public", models.BooleanField(default=False)),
                (
                    "exercice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="herro.exercice"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
