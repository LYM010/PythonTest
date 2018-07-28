#!/usr/bin/env python3
# -*-UTF-8-*-

def displayInventory(inventory):
    print('Inventory:')
    item_total = 0;
    for k,v in inventory.items():
        print(str(v)+' ' +k)
        item_total += v
    print ('\nTotal number of items: '+str(item_total))
    
# inventory:物品清单，字典类型；addedItems:战利品
def addToInventory(inventory,addedItems):
    for i in addedItems:
        if i in inventory.keys():
            inventory[i] +=1
        else:
            inventory.setdefault(i,1)
    return inventory

if __name__ == '__main__':
    stuff = {'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}
    dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
    inv = {'gold coin':42, 'rope':1}
    inv = addToInventory(inv,dragonLoot)
    displayInventory(inv)
    
