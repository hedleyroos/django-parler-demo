# Generated by Django 3.2.6 on 2021-08-17 06:10

from django.db import migrations, models
import django.db.models.deletion
import parler.fields
import parler.models
import photologue.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("photologue", "0010_auto_20160105_1307"),
        ("sites", "0002_alter_domain_unique"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ],
            options={
                "abstract": False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ],
            options={
                "abstract": False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="MyPhoto",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("image", models.ImageField(upload_to=photologue.models.get_storage_path, verbose_name="image")),
                (
                    "date_taken",
                    models.DateTimeField(
                        blank=True,
                        help_text="Date image was taken; is obtained from the image EXIF data.",
                        null=True,
                        verbose_name="date taken",
                    ),
                ),
                ("view_count", models.PositiveIntegerField(default=0, editable=False, verbose_name="view count")),
                (
                    "crop_from",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("top", "Top"),
                            ("right", "Right"),
                            ("bottom", "Bottom"),
                            ("left", "Left"),
                            ("center", "Center (Default)"),
                        ],
                        default="center",
                        max_length=10,
                        verbose_name="crop from",
                    ),
                ),
                (
                    "effect",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="myphoto_related",
                        to="photologue.photoeffect",
                        verbose_name="effect",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="Sensitive",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("sites", models.ManyToManyField(to="sites.Site")),
            ],
            options={
                "abstract": False,
            },
            bases=(parler.models.TranslatableModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="SensitiveTranslation",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("language_code", models.CharField(db_index=True, max_length=15, verbose_name="Language")),
                ("title", models.CharField(max_length=200, verbose_name="Title")),
                (
                    "master",
                    parler.fields.TranslationsForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="parlerdemo.sensitive",
                    ),
                ),
            ],
            options={
                "verbose_name": "sensitive Translation",
                "db_table": "parlerdemo_sensitive_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
                "unique_together": {("language_code", "master")},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="MyPhotoTranslation",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("language_code", models.CharField(db_index=True, max_length=15, verbose_name="Language")),
                ("title", models.CharField(max_length=200, verbose_name="Title")),
                ("parler_image", models.ImageField(upload_to=photologue.models.get_storage_path, verbose_name="Image")),
                (
                    "master",
                    parler.fields.TranslationsForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="parlerdemo.myphoto",
                    ),
                ),
            ],
            options={
                "verbose_name": "my photo Translation",
                "db_table": "parlerdemo_myphoto_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
                "unique_together": {("language_code", "master")},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="CategoryTranslation",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("language_code", models.CharField(db_index=True, max_length=15, verbose_name="Language")),
                ("title", models.CharField(max_length=200, verbose_name="Title")),
                (
                    "master",
                    parler.fields.TranslationsForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="parlerdemo.category",
                    ),
                ),
            ],
            options={
                "verbose_name": "category Translation",
                "db_table": "parlerdemo_category_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
                "unique_together": {("language_code", "master")},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
        migrations.CreateModel(
            name="BlogTranslation",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("language_code", models.CharField(db_index=True, max_length=15, verbose_name="Language")),
                ("title", models.CharField(max_length=200, verbose_name="Title")),
                ("computed", models.CharField(editable=False, max_length=200, null=True)),
                (
                    "category",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="parlerdemo.category"
                    ),
                ),
                (
                    "master",
                    parler.fields.TranslationsForeignKey(
                        editable=False,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="translations",
                        to="parlerdemo.blog",
                    ),
                ),
                ("photos", models.ManyToManyField(blank=True, null=True, to="parlerdemo.MyPhoto")),
                (
                    "sensitive",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="parlerdemo.sensitive"
                    ),
                ),
            ],
            options={
                "verbose_name": "blog Translation",
                "db_table": "parlerdemo_blog_translation",
                "db_tablespace": "",
                "managed": True,
                "default_permissions": (),
                "unique_together": {("language_code", "master")},
            },
            bases=(parler.models.TranslatedFieldsModelMixin, models.Model),
        ),
    ]
