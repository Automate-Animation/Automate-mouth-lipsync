# Generated by Django 4.1.3 on 2022-12-06 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("applipsync", "0012_file_mouth"),
    ]

    operations = [
        migrations.AddField(
            model_name="mouth",
            name="a_e_h",
            field=models.FileField(default=1, upload_to="images/test_normal/"),
            preserve_default=False,
        ),
    ]
