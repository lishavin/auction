# Generated by Django 4.2 on 2023-04-22 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auction_app", "0003_rename_items_item"),
    ]

    operations = [
        migrations.AddField(
            model_name="item",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to=None),
        ),
    ]