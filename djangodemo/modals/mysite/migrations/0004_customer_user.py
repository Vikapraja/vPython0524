# Generated by Django 5.1.4 on 2025-01-23 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mysite", "0003_rename_destination_employee_designation"),
    ]

    operations = [
        migrations.CreateModel(
            name="Customer",
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
                ("name", models.CharField(max_length=30)),
                ("email", models.EmailField(max_length=50)),
                ("city", models.CharField(max_length=50)),
                ("contact", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="User",
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
                ("user_id", models.CharField(max_length=30)),
                ("name", models.CharField(max_length=30)),
                ("password", models.CharField(max_length=30)),
            ],
        ),
    ]
