# Generated by Django 4.2.3 on 2023-07-07 22:00

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Testimonials",
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
                ("photo", models.ImageField(upload_to="testimonials")),
                ("text", models.TextField()),
                ("name", models.CharField(max_length=255)),
            ],
        ),
    ]
