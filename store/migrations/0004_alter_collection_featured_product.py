# Generated by Django 5.0.6 on 2024-06-05 18:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_birthdate_customer_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='featured_product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='store.product'),
        ),
    ]
