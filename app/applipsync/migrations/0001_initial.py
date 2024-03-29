# Generated by Django 4.1.3 on 2022-11-23 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="File",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("audio", models.FileField(upload_to="media/")),
                ("remark", models.CharField(max_length=20)),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
