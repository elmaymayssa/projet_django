# Generated by Django 4.2.7 on 2023-12-02 21:30

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("item", "0002_item"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"ordering": ("name",), "verbose_name_plural": "Categories"},
        ),
    ]
