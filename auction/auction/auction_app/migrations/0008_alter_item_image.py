# Generated by Django 4.2 on 2023-04-23 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auction_app", "0007_rename_create_date_item_create_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="item",
            name="image",
            field=models.ImageField(blank=True, null=True, upload_to="images/"),
        ),
    ]
