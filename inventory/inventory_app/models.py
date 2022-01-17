from django.db import models

# Create your models here.

class Inventory(models.Model):

    # This creates a database called Inventory with the below variables and columns
    name = models.CharField(max_length=30)
    desc = models.CharField(max_length=300)
    qty_in_stock = models.IntegerField()
    unit_price = models.IntegerField()
    inventory_value = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    inventory_id = models.CharField(max_length=20)
    ware_house = models.CharField(max_length=12,
                  blank=False, null=False)
    location_row = models.CharField(max_length=5, blank=False,
                   null=False)
    location_slot = models.CharField(max_length=6, blank=False,
                   null=False)
    shelve =  models.CharField(max_length=12, blank=False,
                null=False)

    # This returns a string of the object using the name of the object
    def __str__(self):
        return f"{self.name}"

    # Decides how the returned values are ordered
    class Meta:
        ordering = ["id"]