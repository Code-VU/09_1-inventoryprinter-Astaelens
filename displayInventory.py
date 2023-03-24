stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'ring': 1, 'apple': 12}

def displayInventory(inventory):
    # your code goes here
    print('Inventory:')
    count=0
    for i in inventory:
        print(inventory[i], i)
        count+=inventory[i]
    print('Total number of items:', count)
if __name__ == "__main__":
    displayInventory(stuff)
