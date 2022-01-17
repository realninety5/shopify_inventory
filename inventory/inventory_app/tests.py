from django.test import TestCase
from .models import Inventory

# Create your tests here.

class InventoryTest(TestCase):
    def setUp(self):
         Inventory.objects.create(name="Spoon", desc="Fine Spoon", qty_in_stock=2, unit_price=2,
                                                      inventory_value=4, ware_house="Ware House 1", location_row="Row 1",
                                                      location_slot="Slot 1", shelve="Shelf 1")

    def inventory_has_value(self):
        # Shows that Inventory saved and has values
        inventory = Inventory.objects.get(name="Spoon")
        self.assertEqual(inventory.name, "Spoon")