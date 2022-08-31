# Generated by Django 4.0 on 2022-08-31 11:28

import django.db.models.deletion
from django.db import migrations, models

import api.custom_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Companies",
            fields=[
                ("index", models.IntegerField(primary_key=True, serialize=False)),
                ("company", models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                "db_table": "companies",
            },
        ),
        migrations.CreateModel(
            name="People",
            fields=[
                ("index", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(blank=True, max_length=128, null=True)),
                ("_id", models.CharField(blank=True, max_length=64, null=True)),
                ("guid", models.CharField(blank=True, max_length=64, null=True)),
                ("has_died", models.BooleanField(blank=True, default=False, null=True)),
                ("balance", models.CharField(blank=True, max_length=64, null=True)),
                ("picture", models.CharField(blank=True, max_length=256, null=True)),
                ("age", models.PositiveIntegerField(blank=True, null=True)),
                ("eyeColor", models.CharField(blank=True, max_length=32, null=True)),
                ("gender", models.CharField(blank=True, max_length=16, null=True)),
                ("email", models.CharField(blank=True, max_length=64, null=True)),
                ("phone", models.CharField(blank=True, max_length=32, null=True)),
                ("address", models.CharField(blank=True, max_length=256, null=True)),
                ("about", models.TextField(blank=True, null=True)),
                ("registered", models.DateTimeField(blank=True, null=True)),
                ("greeting", models.TextField(blank=True, null=True)),
                (
                    "favourite_fruits",
                    api.custom_fields.ListField(blank=True, null=True, token=","),
                ),
                (
                    "favourite_vegetables",
                    api.custom_fields.ListField(blank=True, null=True, token=","),
                ),
                ("tags", api.custom_fields.ListField(blank=True, null=True, token=",")),
                (
                    "company",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="employees",
                        to="api.companies",
                    ),
                ),
                (
                    "friends",
                    models.ManyToManyField(
                        blank=True, related_name="frended", to="api.People"
                    ),
                ),
            ],
            options={
                "db_table": "people",
            },
        ),
    ]
