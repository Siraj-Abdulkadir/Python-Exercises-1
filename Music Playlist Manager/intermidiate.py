# Initialize Playlist
playlist = {}

# Function to Add Song
def add_song(title, artist, duration):
    playlist[title] = (artist, duration)
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

# Function to Calculate Total Duration
def total_duration():
    total = sum(details[1] for details in playlist.values())
    print(f"Total playlist duration: {total} minutes")

# Add Songs and Display Playlist
add_song("Kill Bill", "SZA", 3)
add_song("Anti-Hero", "Taylor Swift", 4)
show_playlist()
total_duration()
