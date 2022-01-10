# Generated by Django 3.2.11 on 2022-01-10 16:13

from django.db import migrations


EVENT_TYPES = ((12, "COMPLETED", "The resourcing request was completed"),)


def insert_event_types(apps, schema_editor):
    EventType = apps.get_model("event_log", "EventType")

    for pk, code, name in EVENT_TYPES:
        EventType.objects.create(pk=pk, code=code, name=name)


def delete_event_types(apps, schema_editor):
    EventType = apps.get_model("event_log", "EventType")

    for pk, _, _ in EVENT_TYPES:
        EventType.objects.get(pk=pk).delete()


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0052_alter_resourcingrequest_state"),
    ]

    operations = [migrations.RunPython(insert_event_types, delete_event_types)]
