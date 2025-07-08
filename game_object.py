from inventory import Inventory


class GameObject:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.inventory = {}

    def print_name(self):
        print(self.name)

    def add_item(self, key, value):
        self.inventory[key] = value

    def remove_item(self, item):
        del self.inventory[item]

    def check_inventory(self):
        for key in self.inventory:
            print(key)

class Scene(GameObject):
    def __init__(self, name, description):
        super().__init__(name, description)


class Player(GameObject):
    def __init__(self, name, description):
        super().__init__(name, description)


class Item(GameObject):
    def __init__(self, name, description):
        super().__init__(name, description)
