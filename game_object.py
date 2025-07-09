class GameObject:
    def __init__(self, name, description, inventory=None):
        self.name = name
        self.description = description
        self.inventory = inventory 

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
        super().__init__(name, description, inventory={})


class Player(GameObject):
    def __init__(self, name, description):
        super().__init__(name, description, inventory={})


class Item(GameObject):
    def __init__(self, name, description):
        super().__init__(name, description)


class Container(GameObject):
    def __init__(self, name, description, is_locked):
        super().__init__(name, description)
        self.is_locked = is_locked
