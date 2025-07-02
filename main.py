from scene import Scene
from scene_connections import SceneConn

connect = SceneConn()
room = Scene("room", "first room in the game")
connect.add_connection("room", north="room_2")
room_2 = Scene("room_2", "second room in the game")
room_3 = Scene("room_3", "third room in the game")

def main():
    print("Welcome to new game!")
    current_room = room
    while True:
        command = input("Would you like to [q]uit or need some [h]elp?")
        if command == 'q':
            print("Quitting game...")
            break
        if command == 'go to room_2':
            current_room = room_2
            print("You are now in room 2.")
            continue
        if command == 'c':
            current_room.print_name()
            continue
        if command == 'h':
            print("this is where the help screen would appear, if I had one.")
        if command == 'north':
            print(connect.connections[current_room.name]["north"])
            continue
        else:
            print("that was not a valid option.")

if __name__ == "__main__":
    main() 
