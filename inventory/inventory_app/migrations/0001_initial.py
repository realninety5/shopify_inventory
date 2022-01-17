# Generated by Django 4.0.1 on 2022-01-16 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('desc', models.CharField(max_length=300)),
                ('qty_in_stock', models.IntegerField()),
                ('unit_price', models.IntegerField()),
                ('inventory_value', models.IntegerField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('inventory_id', models.CharField(max_length=20)),
                ('ware_house', models.CharField(choices=[('w1', 'Ware House 1'), ('w2', 'Ware House 2')], default='w1', max_length=2)),
                ('location_row', models.CharField(choices=[('r1', 'Row 1'), ('r2', 'Row 2'), ('r3', 'Row 3')], default='r1', max_length=2)),
                ('location_slot', models.CharField(choices=[('s1', 'Slot 1'), ('s2', 'Slot 2'), ('s3', 'Slot 3'), ('s4', 'Slot 4'), ('s5', 'Slot 5')], default='s1', max_length=2)),
                ('shelve', models.CharField(choices=[('sh1', 'Shelf 1'), ('sh2', 'Shelf 2'), ('sh3', 'Shelf 3'), ('sh4', 'Shelf 4'), ('sh5', 'Shelf 5'), ('sh6', 'Shelf 6'), ('sh7', 'Shelf 7'), ('sh8', 'Shelf 8'), ('sh9', 'Shelf 9'), ('sh10', 'Shelf 10'), ('sh11', 'Shelf 11'), ('sh12', 'Shelf 12'), ('sh13', 'Shelf 13'), ('sh14', 'Shelf 14'), ('sh15', 'Shelf 15')], default='sh1', max_length=4)),
            ],
            options={
                'ordering': ['-created'],
            },
        ),
    ]
