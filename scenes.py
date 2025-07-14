from game_object import Scene, Item, Container, Enemy 
from scene_connections import SceneConn

# Create all the scenes you need for your game here
room_1 = Scene("room_1", "starting room")
room_2 = Scene("room_2", "middle room with combat")
room_3 = Scene("room_3", "last room with chest")

# SceneConnections instance do not alter the line below
connect = SceneConn()

# Create connections to all of the above scenes
connect.add_connection(room_1.name, north=room_2)
connect.add_connection(room_2.name, east=room_3, south=room_1)
connect.add_connection(room_3.name, west=room_2)

# Create items here
key = Item('key', 'key for opening chests and doors')

# Add containers to game
chest_1 = Container("chest", "A Locked Chest", True)

# Add enemies here
goblin = Enemy("Goblin", "An enemy holding a key", 100, 20)

# Add items to Enemy inventories here
goblin.add_item(key.name, key)

# Add items, containers, and enemies to starting locations
room_3.add_item(chest_1.name, chest_1)
room_2.add_item(goblin.name, goblin)
goblin.add_item(key, key)

