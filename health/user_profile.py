import json

def view_profile(user):
    print(user)

def update_contact_number(user, users):
    new_contact = input("Enter your new contact number: ")
    user.contact_number = new_contact
    save_users(users, 'fitness_data.json')
    print("Phone number updated")

def save_users(users, filename):
    with open(filename, 'w') as file:
        json.dump([user.to_dict() for user in users], file, indent=4)

def stats(user, users):
    weight = input("What is your current weight? ")
    waist = input("What is your desired waist size? ")

def desired_stats(user, users):
    height = input("What is your height? ")
    desired_weight = input("What is your desired weight? ")
    desired_waist = input("What is your desired waist size? ")

def user_profile_menu(user, users):
    while True:
        print("\nWelcome to your user profile.")
        print("'view' profile")
        print("'update' contact number")
        print("'change' stats")
        print("'desired' stats")
        print("'exit' to return to the main menu")
        choice = input("What would you like to do? ")

        if choice == 'view':
            view_profile(user)
        elif choice == 'update':
            update_contact_number(user, users)
        elif choice == 'change':
            stats(user, users)
        elif choice == 'desired':
            desired_stats(user, users)
        elif choice == 'exit':
            print("Returning to main menu...")
            break
        else:
            print("Invalid input, please try again")
