# Generated by Django 3.2.11 on 2022-01-10 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0051_interimrequest_overseas_country"),
    ]

    operations = [
        migrations.AlterField(
            model_name="resourcingrequest",
            name="state",
            field=models.SmallIntegerField(
                choices=[
                    (0, "Draft"),
                    (1, "Awaiting approvals"),
                    (2, "Amending"),
                    (3, "Amendments review"),
                    (4, "Approved"),
                    (5, "Completed"),
                ],
                default=0,
                verbose_name="Status",
            ),
        ),
    ]
