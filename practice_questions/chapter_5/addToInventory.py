import pprint
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'ruby', 'rope']
#inv = {'gold coin':42, 'rope':1}
inv = {}

def addToInventory(inventory, addItems):
    for item in addItems:
        inventory.setdefault(item, 0)

    for item in addItems:
         if item in inventory:
             inventory[item] += 1
    return inventory

myInventory = addToInventory(inv, dragonLoot)
pprint.pprint(myInventory)

             
