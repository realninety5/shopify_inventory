# Generated by Django 4.0.1 on 2022-01-17 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0003_alter_inventory_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventory',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='inventory',
            name='location_row',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='location_slot',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='shelve',
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name='inventory',
            name='ware_house',
            field=models.CharField(max_length=12),
        ),
    ]
