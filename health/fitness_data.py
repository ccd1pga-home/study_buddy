def add_fitness_data(user, users):
    # Implementation for adding fitness data
    pass

def view_fitness_data(user):
    # Implementation for viewing fitness data
    pass

def fitness_data_menu(user, users):
    while True:
        print("\nWelcome to your fitness data.")
        print("'add' fitness data")
        print("view fitness 'data'")
        print("'exit' to return to the main menu")
        choice = input("What would you like to do? ")

        if choice == 'add':
            add_fitness_data(user, users)
        elif choice == 'data':
            view_fitness_data(user)
        elif choice == 'exit':
            print("Returning to main menu...")
            break
        else:
            print("Invalid input, please try again")
