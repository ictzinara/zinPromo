# Generated by Django 4.1.7 on 2023-03-01 06:52

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="PromotionApplicant",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4, primary_key=True, serialize=False
                    ),
                ),
                ("reg_number", models.CharField(max_length=100)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("email", models.CharField(max_length=50)),
                ("nat_id", models.CharField(max_length=50)),
                ("phone", models.CharField(max_length=50)),
                ("City", models.CharField(max_length=100)),
                ("application_date", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Province",
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
                ("name", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="PromotionWeeklyDraw",
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
                ("notified", models.BooleanField(default=False)),
                ("notified_on", models.DateField()),
                ("price_claimed", models.BooleanField(default=False)),
                (
                    "weekly_winner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Api.promotionapplicant",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GrandPriceDraw",
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
                ("position", models.IntegerField(default=0)),
                ("notified", models.BooleanField(default=False)),
                ("notified_on", models.DateField()),
                ("price_claimed", models.BooleanField(default=False)),
                (
                    "weekly_winner",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="Api.promotionapplicant",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="City",
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
                ("description", models.CharField(max_length=50)),
                (
                    "province",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="Api.province"
                    ),
                ),
            ],
        ),
    ]