import spotipy
from spotipy.oauth2 import SpotifyOAuth
from collections import deque

# Spotify API credentials
client_id = '14a5c95dc664471599ccfaf532ba51a6'
client_secret = '6c9eb1848f4c486b896b75da7f974776'
redirect_uri = 'http://localhost:8888/callback'

# Spotify scope for modifying playlists and streaming music
scope='playlist-read-private user-modify-playback-state user-read-playback-state'
# Authenticate with Spotify
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope=scope))

# 플레이리스트 ID
# playlist_id = 'spotify:playlist:4r53elEnWIyPxK0FaMtK7s'
# https://open.spotify.com/playlist/4r53elEnWIyPxK0FaMtK7s?si=5ee94745f26148df


def get_playlist_tracks(playlist_id):
    results = sp.playlist_tracks(playlist_id)
    return [track['track']['id'] for track in results['items']]

def play_track(track_id):
    sp.start_playback(uris=[f'spotify:track:{track_id}'])

def pause_playback():
    sp.pause_playback()

def next_track():
    sp.next_track()

def previous_track():
    sp.previous_track()

def main():
    playlist_id_1 = 'spotify:playlist:0ngtkz0NLxvfno6qBqqXOr'
    playlist_id_2 = 'spotify:playlist:4IWKuYFX3yg4x7JvhafmiL'

    tracks_playlist_1 = get_playlist_tracks(playlist_id_1)
    tracks_playlist_2 = get_playlist_tracks(playlist_id_2)

    playlist_1_queue = deque(tracks_playlist_1)
    playlist_2_queue = deque(tracks_playlist_2)

    current_playlist = 1
    current_track = None
    previous_track_id = None

    while True:
        if not playlist_1_queue and not playlist_2_queue:
            print("Both playlists are empty.")
            break

        if current_playlist == 1 and playlist_1_queue:
            current_track = playlist_1_queue.popleft()
        elif current_playlist == 2 and playlist_2_queue:
            current_track = playlist_2_queue.popleft()

        if current_track:
            if previous_track_id:
                previous_track_id = current_track

            play_track(current_track)
            print(f"Playing track {current_track} from playlist {current_playlist}")

            current_playlist = 2 if current_playlist == 1 else 1

        # Example controls for demonstration
        command = input("Enter command (play/pause/next/previous/quit): ").strip().lower()

        if command == 'pause':
            pause_playback()
        elif command == 'next':
            next_track()
            if previous_track_id:
                previous_track_id = current_track
            current_track = None
        elif command == 'previous':
            if previous_track_id:
                play_track(previous_track_id)
                previous_track_id = current_track
                current_track = None
        elif command == 'quit':
            break

if __name__ == "__main__":
    main()
