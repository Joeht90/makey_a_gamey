from game_object import Player
from scene_connections import SceneConn
import scenes as s
scenes = s.connect

def main():
    print("Welcome to new game!")
    location = s.room_1
    player_1 = Player('player_1', 'Your character for the game.')
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
        if command == 'li':
            location.check_inventory()
            continue
        if command == 'ci':
            player_1.check_inventory()
            continue
        if 'open' in command:
            chest = command.split()
            if 'key' in player_1.inventory and location.inventory[chest[-1]].is_locked == True:
                location.inventory[chest[-1]].is_locked = False
                player_1.remove_item('key')
                print("You win!")
                break
            elif 'key' not in player_1.inventory and location.inventory[chest[-1]].is_locked == True:
                print("You do not have a key in your inventory!")
            continue
        if 'take' in command:
            item = command.split()
            player_1.add_item(item[-1], location.inventory[item[-1]])
            location.remove_item(item[-1])
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
