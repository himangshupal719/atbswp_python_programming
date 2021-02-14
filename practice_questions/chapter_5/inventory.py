def displayInventory(inventory):
    item_total = 0
    print("Inventory")
    for item, count in inventory.items():
        item_total += count
        print(str(count)+' '+item)
    print("Total number of items: "+str(item_total))


def addToInventory(inventory, addItems):
    for item in addItems:
        inventory.setdefault(item, 0)

    for item in addItems:
         if item in inventory:
             inventory[item] += 1
    return inventory



dragonLoot = ['gold coin', 'dagger', 'gold coin', 'ruby', 'rope']
stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}

myInventory = addToInventory(stuff, dragonLoot)
displayInventory(myInventory)


