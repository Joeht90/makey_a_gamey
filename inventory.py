class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item):
        self.inventory[item.name] = item

    def remove_item(self, item):
        del self.inventory[item]

    def check_inventory(self):
        for key in self.inventory:
            print(key)
