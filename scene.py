from inventory import Inventory


class GameObject:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def print_name(self):
        print(self.name)


class Scene(GameObject):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.inventory = Inventory()


class Item:
    def __init__(self, name, description):
        super().__init__(name, description)
