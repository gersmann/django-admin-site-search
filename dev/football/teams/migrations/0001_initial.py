# Generated by Django 4.1.7 on 2023-03-15 19:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("players", "0001_initial"),
        ("stadiums", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Team",
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
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                (
                    "name",
                    models.CharField(
                        help_text="The official name of the football team",
                        max_length=120,
                    ),
                ),
                (
                    "key",
                    models.SlugField(
                        help_text="Unique key, used in URLs and code references",
                        max_length=120,
                        unique=True,
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("CLUB", "Club"), ("NATIONAL", "National")],
                        help_text="The type of team",
                        max_length=10,
                    ),
                ),
                ("website", models.URLField(help_text="Link to the official website")),
                (
                    "stadium",
                    models.ForeignKey(
                        blank=True,
                        help_text="The stadium that the team currently plays in, as home",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="stadiums.stadium",
                    ),
                ),
            ],
            options={
                "ordering": ["created_at"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Squad",
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
                ("created_at", models.DateTimeField(auto_now_add=True, null=True)),
                ("updated_at", models.DateTimeField(auto_now=True, null=True)),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("SENIOR_MEN", "Senior men's team"),
                            ("SENIOR_WOMEN", "Senior women's team"),
                            ("ACADEMY", "Academy"),
                            ("CHARITY", "Charity team"),
                        ],
                        help_text="The type of squad",
                        max_length=20,
                    ),
                ),
                (
                    "players",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Football players in this team/squad",
                        to="players.player",
                    ),
                ),
                (
                    "team",
                    models.ForeignKey(
                        help_text="The team that owns this squad",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="teams.team",
                    ),
                ),
            ],
            options={
                "ordering": ["created_at"],
                "abstract": False,
            },
        ),
    ]