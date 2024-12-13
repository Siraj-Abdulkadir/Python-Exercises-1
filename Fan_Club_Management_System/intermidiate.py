# Dictionary to Store Fan Details
fan_details = {}

# Function to Add a Member
def add_member(name, age, favorite_character):
    fan_details[name] = (age, favorite_character)
    print(f"{name} has been added to the club!")

# Function to Find Members by Favorite Character
def find_by_favorite_character(character):
    for name, details in fan_details.items():
        if details[1] == character:
            print(f"{name}, Age: {details[0]}")

# Add Members
add_member("Ruth", 28, "Chandler")
add_member("Miki", 30, "Joey")

# Find Members by Character
print("Fans who love Chandler:")
find_by_favorite_character("Chandler")
