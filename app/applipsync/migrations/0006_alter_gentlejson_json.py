# Generated by Django 4.1.3 on 2022-11-28 06:25

import jsonfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("applipsync", "0005_gentlejson_json"),
    ]

    operations = [
        migrations.AlterField(
            model_name="gentlejson",
            name="json",
            field=jsonfield.fields.JSONField(null=True),
        ),
    ]