# Generated by Django 4.1.3 on 2022-12-12 11:02

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("applipsync", "0019_alter_file_audio"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mouth",
            name="a_e_h",
            field=models.FileField(
                upload_to="images/test_normal/",
                validators=[django.core.validators.FileExtensionValidator(["png"])],
            ),
        ),
        migrations.AlterField(
            model_name="mouth",
            name="d_j_ch_h",
            field=models.FileField(
                upload_to="images/test_normal/",
                validators=[django.core.validators.FileExtensionValidator(["png"])],
            ),
        ),
        migrations.AlterField(
            model_name="mouth",
            name="f_h",
            field=models.FileField(
                upload_to="images/test_normal/",
                validators=[django.core.validators.FileExtensionValidator(["png"])],
            ),
        ),
        migrations.AlterField(
            model_name="mouth",
            name="l_h",
            field=models.FileField(
                upload_to="images/test_normal/",
                validators=[django.core.validators.FileExtensionValidator(["png"])],
            ),
        ),
        migrations.AlterField(
            model_name="mouth",
            name="m_b_close_h",
            field=models.FileField(
                upload_to="images/test_normal/",
                validators=[django.core.validators.FileExtensionValidator(["png"])],
            ),
        ),
        migrations.AlterField(
            model_name="mouth",
            name="o_big_h",
            field=models.FileField(
                upload_to="images/test_normal/",
                validators=[django.core.validators.FileExtensionValidator(["png"])],
            ),
        ),
        migrations.AlterField(
            model_name="mouth",
            name="o_small_h",
            field=models.FileField(
                upload_to="images/test_normal/",
                validators=[django.core.validators.FileExtensionValidator(["png"])],
            ),
        ),
        migrations.AlterField(
            model_name="mouth",
            name="oh_h",
            field=models.FileField(
                upload_to="images/test_normal/",
                validators=[django.core.validators.FileExtensionValidator(["png"])],
            ),
        ),
        migrations.AlterField(
            model_name="mouth",
            name="th_h",
            field=models.FileField(
                upload_to="images/test_normal/",
                validators=[django.core.validators.FileExtensionValidator(["png"])],
            ),
        ),
        migrations.AlterField(
            model_name="mouth",
            name="trans_h",
            field=models.FileField(
                upload_to="images/test_normal/",
                validators=[django.core.validators.FileExtensionValidator(["png"])],
            ),
        ),
    ]
