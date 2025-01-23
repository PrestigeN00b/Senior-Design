def move_forward():
    print("Rover is moving forward...")

def turn_left():
    print("Rover is turning left...")

def turn_right():
    print("Rover is turning right...")

def stop():
    print("Rover has stopped.")

def display_menu():
    print("\nRover Control Menu:")
    print("1. Move Forward")
    print("2. Turn Left")
    print("3. Turn Right")
    print("4. Stop")
    print("5. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            move_forward()
        elif choice == "2":
            turn_left()
        elif choice == "3":
            turn_right()
        elif choice == "4":
            stop()
        elif choice == "5":
            print("Exiting rover simulation. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()