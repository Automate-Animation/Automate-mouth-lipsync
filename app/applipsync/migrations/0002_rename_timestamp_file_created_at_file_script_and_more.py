# Generated by Django 4.1.3 on 2022-11-23 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("applipsync", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="file",
            old_name="timestamp",
            new_name="created_at",
        ),
        migrations.AddField(
            model_name="file",
            name="script",
            field=models.FileField(default="h", upload_to="script/"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="file",
            name="audio",
            field=models.FileField(upload_to="audio/"),
        ),
    ]
