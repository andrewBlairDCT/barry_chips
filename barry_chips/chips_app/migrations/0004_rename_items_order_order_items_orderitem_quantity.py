# Generated by Django 5.1.4 on 2025-01-06 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chips_app', '0003_remove_order_items_order_items'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='items',
            new_name='order_items',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
