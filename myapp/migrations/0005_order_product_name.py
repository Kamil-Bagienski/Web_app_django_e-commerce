# Generated by Django 5.0 on 2024-01-14 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_order_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]