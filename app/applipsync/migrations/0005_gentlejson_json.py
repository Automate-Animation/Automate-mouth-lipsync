# Generated by Django 4.1.3 on 2022-11-28 06:20

import jsonfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("applipsync", "0004_remove_gentlejson_json"),
    ]

    operations = [
        migrations.AddField(
            model_name="gentlejson",
            name="json",
            field=jsonfield.fields.JSONField(default=1),
            preserve_default=False,
        ),
    ]
