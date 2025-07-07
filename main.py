from scene import Scene
from scene_connections import SceneConn
from inventory import Inventory
import scenes as s
scenes = s.connect

def main():
    print("Welcome to new game!")
    location = s.room_1
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
        if command == 'i':
            location.inventory.check_inventory()
            continue
        if 'take' in command:
            item = command.split()
            location.inventory.remove_item(item[-1])
            continue
        if 'go' in command:
            direction = command.split()
            try:
                if scenes.connections[location.name][direction[-1]] == None:
                    print("You cannot go that direction!")
                    continue
                location = scenes.move_room(location.name, direction[-1])
            except KeyError:
                print("I'm not sure what you are asking. Try again.")
            continue
        else:
            print("that was not a valid option.")


if __name__ == "__main__":
    main() 
