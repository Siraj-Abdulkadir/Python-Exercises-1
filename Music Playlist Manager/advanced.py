# Initialize Playlist
playlist = {}
song_titles = set()

# Function to Add Song
def add_song(title, artist, duration):
    if title in song_titles:
        print(f"'{title}' is already in the playlist!")
    else:
        playlist[title] = (artist, duration)
        song_titles.add(title)
        print(f"'{title}' by {artist} ({duration} mins) added to the playlist!")

# Function to Show Playlist
def show_playlist():
    if not playlist:
        print("The playlist is empty.")
    else:
        print("Your playlist:")
        for title, details in playlist.items():
            artist, duration = details
            print(f"- '{title}' by {artist} ({duration} mins)")

# Function to Remove a Song
def remove_song(title):
    if title in song_titles:
        del playlist[title]
        song_titles.remove(title)
        print(f"'{title}' has been removed from the playlist!")
    else:
        print(f"'{title}' is not in the playlist!")

# Function to Search for a Song
def search_song(title):
    if title in playlist:
        artist, duration = playlist[title]
        print(f"'{title}' by {artist} ({duration} mins) is in the playlist.")
    else:
        print(f"'{title}' is not in the playlist.")

# Menu System
while True:
    print("\n1. Add Song")
    print("2. Show Playlist")
    print("3. Remove Song")
    print("4. Search Song")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        title = input("Enter song title: ")
        artist = input("Enter artist name: ")
        duration = int(input("Enter duration (in mins): "))
        add_song(title, artist, duration)
    elif choice == "2":
        show_playlist()
    elif choice == "3":
        title = input("Enter song title to remove: ")
        remove_song(title)
    elif choice == "4":
        title = input("Enter song title to search: ")
        search_song(title)
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.")
