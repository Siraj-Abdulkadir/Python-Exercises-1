# Initialize Playlist
playlist = []

# Function to Add Song
def add_song(song_title):
    playlist.append(song_title)
    print(f"'{song_title}' has been added to the playlist!")

# Function to Show Playlist
def show_playlist():
    if len(playlist) == 0:
        print("The playlist is empty.")
    else:
        print("Your playlist:")
        for song in playlist:
            print(f"- {song}")

# Add Songs and Show Playlist
add_song("Lauren Hills - EX-Factor")
add_song("Kanye West - Good Morning")
show_playlist()
