# Generated by Django 4.2 on 2023-04-22 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("auction_app", "0001_initial"),
    ]

    operations = [
        migrations.RenameModel(old_name="Goods", new_name="items",),
    ]