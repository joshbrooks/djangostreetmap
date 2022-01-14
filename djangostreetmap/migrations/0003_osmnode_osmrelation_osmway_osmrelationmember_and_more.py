# Generated by Django 4.0 on 2022-01-14 02:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djangostreetmap", "0002_delete_osmadminboundary_alter_overpassquery_name_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="OsmNode",
            fields=[
                ("id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("lat", models.FloatField()),
                ("lon", models.FloatField()),
                ("srid", models.IntegerField(blank=True, null=True)),
                ("tags", models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="OsmRelation",
            fields=[
                ("id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("tags", models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="OsmWay",
            fields=[
                ("id", models.BigIntegerField(primary_key=True, serialize=False)),
                ("tags", models.JSONField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="OsmRelationMember",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("ordinality", models.IntegerField()),
                ("node", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="djangostreetmap.osmnode")),
                ("way", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="djangostreetmap.osmway")),
            ],
        ),
        migrations.CreateModel(
            name="OsmNodeWay",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("ordinality", models.IntegerField()),
                ("node", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="djangostreetmap.osmnode")),
                ("way", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="djangostreetmap.osmway")),
            ],
        ),
        migrations.AddConstraint(
            model_name="osmnodeway",
            constraint=models.UniqueConstraint(fields=("way", "ordinality"), name="unique_ordinality"),
        ),
    ]
