from scene import Scene
from scene_connections import SceneConn
import scenes


def main():
    print("Welcome to new game!")
    location = scenes.room_1
    while True:
        command = input("Would you like to [q]uit or need some [h]elp?")
        if command == 'q':
            print("Quitting game...")
            break
        if command == 'c':
            location.print_name()
            continue
        if command == 'h':
            print("this is where the help screen would appear, if I had one.")
        if 'go' in command:
            direction = command.split()
            if scenes.connect.connections[location.name][direction[-1]] == None:
                print("You cannot go that direction!")
                continue
            location = scenes.connect.move_room(location.name, direction[-1])
            continue
        else:
            print("that was not a valid option.")


if __name__ == "__main__":
    main() 
