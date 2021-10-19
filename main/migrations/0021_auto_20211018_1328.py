# Generated by Django 3.2.8 on 2021-10-18 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0020_contractorapproval_requestor"),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name="contractorapproval",
            name="check_status",
        ),
        migrations.AlterField(
            model_name="contractorapproval",
            name="status",
            field=models.SmallIntegerField(
                choices=[
                    (0, "Draft"),
                    (1, "Awaiting chief approval"),
                    (2, "Awaiting approvals"),
                    (3, "Approved"),
                ],
                default=0,
            ),
        ),
        migrations.AddIndex(
            model_name="contractorapproval",
            index=models.Index(fields=["status"], name="status_index"),
        ),
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
                    models.Q(
                        ("commercial_approval__isnull", True),
                        ("finance_approval__isnull", True),
                        ("hrbp_approval__isnull", True),
                        ("status", 1),
                    ),
                    models.Q(("chief_approval", True), ("status", 2)),
                    models.Q(
                        ("chief_approval", True),
                        ("commercial_approval", True),
                        ("finance_approval", True),
                        ("hrbp_approval", True),
                        ("status", 3),
                    ),
                    _connector="OR",
                ),
                name="check_status",
            ),
        ),
    ]
