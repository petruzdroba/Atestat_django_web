# Generated by Django 4.2.7 on 2023-12-29 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PopularProductModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('product_id', models.IntegerField()),
                ('price', models.FloatField()),
                ('author', models.CharField(max_length=150)),
                ('gif', models.CharField(max_length=255)),
            ],
        ),
    ]