from game_object import Scene, Item 
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

# Add items to starting inventories
room_2.inventory.add_item(key)
