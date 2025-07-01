def main():
    print("Welcome to new game!")
    while True:
        command = input("Would you like to [q]uit or need some [h]elp?")
        if command == 'q':
            break
        if command == 'h':
            print("this is where the help screen would appear, if I had one.")
        else:
            print("that was not a valid option.")

if __name__ == "__main__":
    main()
