import random

# Initialize Fan Club
fan_details = {}
fan_names = set()

# Function to Add Member
def add_member(name, age, favorite_character):
    if name in fan_names:
        print(f"{name} is already a member!")
    else:
        fan_names.add(name)
        fan_details[name] = {"age": age, "favorite_character": favorite_character}
        print(f"{name} has been added to the fan club!")

# Function to Show Members
def show_members():
    if not fan_details:
        print("The fan club has no members yet.")
    else:
        print("\nFan Club Members:")
        for name, details in fan_details.items():
            print(f"- {name}, Age: {details['age']}, Favorite Character: {details['favorite_character']}")

# Function to Remove a Member
def remove_member(name):
    if name in fan_names:
        del fan_details[name]
        fan_names.remove(name)
        print(f"{name} has been removed from the fan club!")
    else:
        print(f"{name} is not in the fan club!")

# Function to Search for a Member
def search_member(name):
    if name in fan_details:
        details = fan_details[name]
        print(f"Found: {name}, Age: {details['age']}, Favorite Character: {details['favorite_character']}")
    else:
        print(f"{name} is not a member of the fan club.")

# Function to Select Fan of the Month
def fan_of_the_month():
    if not fan_details:
        print("No members in the fan club to choose from.")
    else:
        winner = random.choice(list(fan_names))
        details = fan_details[winner]
        print(f"\n🎉 Fan of the Month: {winner} 🎉")
        print(f"Age: {details['age']}, Favorite Character: {details['favorite_character']}")

# Menu System
while True:
    print("\n1. Add Member")
    print("2. Show Members")
    print("3. Remove Member")
    print("4. Search Member")
    print("5. Select Fan of the Month")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ")
        age = int(input("Enter age: "))
        favorite_character = input("Enter favorite character: ")
        add_member(name, age, favorite_character)
    elif choice == "2":
        show_members()
    elif choice == "3":
        name = input("Enter the name of the member to remove: ")
        remove_member(name)
    elif choice == "4":
        name = input("Enter the name of the member to search: ")
        search_member(name)
    elif choice == "5":
        fan_of_the_month()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
