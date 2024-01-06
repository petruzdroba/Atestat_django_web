# Generated by Django 4.2.7 on 2024-01-04 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_backend', '0008_customuser_other_ids'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='other_ids',
        ),
        migrations.AddField(
            model_name='customuser',
            name='created_products_id',
            field=models.ManyToManyField(blank=True, related_name='created_products', to='web_backend.customuser'),
        ),
    ]