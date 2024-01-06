# Generated by Django 4.2.7 on 2024-01-06 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_backend', '0011_remove_customuser_created_products_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='created_products',
        ),
        migrations.AddField(
            model_name='customuser',
            name='created_products',
            field=models.JSONField(blank=True, null=True),
        ),
    ]