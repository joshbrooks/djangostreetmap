# Generated by Django 4.0 on 2022-01-14 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("djangostreetmap", "0005_osmrelationmember_relation"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="osmrelationmember",
            constraint=models.UniqueConstraint(fields=("relation", "ordinality"), name="unique_ordinality_rel"),
        ),
    ]
