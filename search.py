import os
import random
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from taglist import tags

# Code adapted from ChatGPT query
# Conversation link: https://chat.openai.com/share/fba058db-2fdf-42de-8af1-e6c26293c063

load_dotenv()
client_id = os.environ.get("SPOTIFY_CLIENT_ID")
client_secret = os.environ.get("SPOTIFY_CLIENT_SECRET")

print("Client ID:", client_id)
print("Client Secret:", client_secret)

# Initialize the Spotify API client
auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

def generate_random_query():
    query_elements = []
    
    # Generate a random alphanumeric string
    alphanumeric_string = ''.join(random.choices('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=5))
    query_elements.append(alphanumeric_string)
    
    # Randomly select tags
    tag_selection = random.sample(tags, 3)
    query_elements.extend(tag_selection)
    
    return ' '.join(query_elements)

def discover_random_music():
    query = generate_random_query()
    print('Query:', query)
    
    results = sp.search(query, type='artist', limit=10)
    artists = results['artists']['items']
    print('Artists:', [a['name'] for a in artists])
    
    if not artists:
        return None
    
    random_artist = random.choice(artists)
    print('Selected Artist:', random_artist['name'])
    
    top_tracks = sp.artist_top_tracks(random_artist['id'])['tracks']
    
    if not top_tracks:
        return None
    
    print('Top tracks:', [t['name'] for t in top_tracks])
    random_track = random.choice(top_tracks)
    print('Selected track:', random_track['name'])
    
    return random_track['external_urls']['spotify']

if __name__ == "__main__":
    random_track_url = discover_random_music()
    if random_track_url:
        print("Enjoy your random music discovery:")
        print(random_track_url)
    else:
        print("No random music found.")
