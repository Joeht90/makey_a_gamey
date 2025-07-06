from scene import Scene
from scene_connections import SceneConn
import scenes


def main():
    print("Welcome to new game!")
    current_room = scenes.room_1
    while True:
        command = input("Would you like to [q]uit or need some [h]elp?")
        if command == 'q':
            print("Quitting game...")
            break
        if command == 'c':
            current_room.print_name()
            continue
        if command == 'h':
            print("this is where the help screen would appear, if I had one.")
        if command == 'north':
            # TODO: clean up the scenes.connect.move_room, that is a lot of code
            # we do not need but it works for now
            current_room = scenes.connect.move_room(current_room.name, "north")
            print(current_room)
            continue
        else:
            print("that was not a valid option.")


if __name__ == "__main__":
    main() 
