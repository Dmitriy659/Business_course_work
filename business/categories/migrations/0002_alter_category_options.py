# Generated by Django 5.1.3 on 2024-11-23 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("categories", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={
                "ordering": ("-title",),
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
    ]
