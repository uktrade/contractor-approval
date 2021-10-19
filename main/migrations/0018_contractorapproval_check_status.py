# Generated by Django 3.2.8 on 2021-10-15 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0017_contractorapproval_chief"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="contractorapproval",
            constraint=models.CheckConstraint(
                check=models.Q(
                    models.Q(
                        ("chief_approval__isnull", True),
                        ("commercial_approval__isnull", True),
                        ("finance_approval__isnull", True),
                        ("hrbp_approval__isnull", True),
                        ("status", 0),
                    ),
                    ("status", 1),
                    _connector="OR",
                ),
                name="check_status",
            ),
        ),
    ]
