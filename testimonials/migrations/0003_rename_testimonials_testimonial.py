# Generated by Django 4.2.3 on 2023-07-07 22:42

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("testimonials", "0002_rename_text_testimonials_testimonial_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Testimonials",
            new_name="Testimonial",
        ),
    ]