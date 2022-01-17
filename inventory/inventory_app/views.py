from django.shortcuts import render
from django.http import HttpResponse
from .models import Inventory

# Create your views here.


def index(request):

    # Checks if the request is POST, if POST, it persists it to the DB
    if request.method == "POST":
            name = request.POST["name"]
            desc = request.POST["desc"]
            qty_in_stock = request.POST["qty_in_stock"]
            unit_price = request.POST["unit_price"]
            inventory_value = int(qty_in_stock) * int(unit_price)
            ware_house = request.POST["ware_house"]
            location_row = request.POST["location_row"]
            location_slot = request.POST["location_slot"]
            shelve = request.POST["shelve"]
            i = Inventory(name=name, desc=desc, qty_in_stock=qty_in_stock, unit_price=unit_price,
                     inventory_value=inventory_value, ware_house=ware_house, location_row=location_row,
                     location_slot=location_slot, shelve=shelve)
            i.save()

    # Get all objects in the database and returns to the frontend
    inventories = Inventory.objects.all()
    return render(request, "inventory_app/layout.html",
                  {'inventories': inventories})


def delete(request, id):
    try:
        inventory = Inventory.objects.get(id=id)
        if inventory.qty_in_stock >= 1:
            inventory.qty_in_stock -= 1
            inventory.inventory_value = inventory.qty_in_stock * inventory.unit_price
            inventory.save()
        if inventory.qty_in_stock <= 0:
            inventory.delete()
    except Inventory.DoesNotExist:
        inventories = Inventory.objects.all()


    inventories = Inventory.objects.all()
    return render(request, "inventory_app/layout.html",
                  {'inventories': inventories})
