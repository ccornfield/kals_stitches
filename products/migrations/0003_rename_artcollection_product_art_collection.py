# Generated by Django 5.1.4 on 2025-01-07 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_rename_art_collection_product_artcollection'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='artcollection',
            new_name='art_collection',
        ),
    ]
