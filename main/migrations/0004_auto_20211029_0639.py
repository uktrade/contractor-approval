# Generated by Django 3.2.8 on 2021-10-29 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20211028_1022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interimrequest',
            name='new_requirement',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], verbose_name='New'),
        ),
        migrations.AlterField(
            model_name='interimrequest',
            name='uk_based',
            field=models.BooleanField(choices=[(True, 'Yes'), (False, 'No')], default=True, verbose_name='UK based'),
        ),
    ]
