# Variables and List
fan_club_name = "Friends Forever Club"
members = ["Abebe", "Melaku", "Meron", "Lidya", "Kirubel", "Fitsum"]
favorite_characters = ["Chandler", "Joey", "Rachel"]

# Function to Check Membership
def is_valid_member(name):
    if name in members:
        return True
    else:
        return False

# Test the function
member_name = "Meron"
if is_valid_member(member_name):
    print(f"Welcome to {fan_club_name}, {member_name}!")
else:
    print("Sorry, you are not a registered member.")
