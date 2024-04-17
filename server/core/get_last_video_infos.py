import os
import json
from datetime import datetime, timedelta
from googleapiclient.discovery import build

from dotenv import load_dotenv
load_dotenv()

# Path to credentials.json
credential_path = os.path.join(os.path.dirname(__file__), 'credentials.json')
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path

# Define your playlist ID
playlist_id = os.getenv("YOUTUBE_PLAYLIST_ID")
# Define your API key
YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

# Create a PlaylistCache class to manage caching
class PlaylistCache:
    def __init__(self, playlist_id, latest_episode, expiration_date):
        self.playlist_id = playlist_id
        self.latest_episode = latest_episode
        self.expiration_date = expiration_date

    def get_latest_episode(self):
        return self.latest_episode

    def is_expired(self):
        return datetime.now() > self.expiration_date

# Initialize a YouTube service
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

# Function to retrieve the latest episode from the playlist
def get_latest_episode(playlist_id):
    playlist_cache = json.loads(get_playlist_cache(playlist_id))

    if playlist_cache and not is_expired(playlist_cache["expiration_date"]):
        return playlist_cache["latest_episode"]
    
    items = youtube.playlistItems().list(
        part="snippet",
        playlistId=playlist_id,  # Include the playlistId parameter
        maxResults=50
    ).execute()

    while "nextPageToken" in items:
        next_page_token = items["nextPageToken"]
        items = youtube.playlistItems().list(
            part="snippet",
            playlistId=playlist_id,
            maxResults=50,
            pageToken=next_page_token
        ).execute()

    latest_video_id = items["items"][-1]["snippet"]["resourceId"]["videoId"]
    latest_video = youtube.videos().list(
        part="snippet",
        id=latest_video_id
    ).execute()

    latest_episode = latest_video["items"][0]
    expiration_date = datetime.now() + timedelta(days=1)  # Cache expiration in 24 hours

    update_playlist_cache(playlist_id, latest_episode, expiration_date)

    return latest_episode

# Function to retrieve playlist cache from storage
def get_playlist_cache(playlist_id):
    cache_file_path = f"playlist_cache_{playlist_id}.json"
    if os.path.exists(cache_file_path):
        with open(cache_file_path, "r") as f:
            return f.read()
    else:
        return "{}"  # Return empty JSON object if cache file doesn't exist

# Function to update playlist cache in storage
def update_playlist_cache(playlist_id, latest_episode, expiration_date):
    playlist_cache = PlaylistCache(playlist_id, latest_episode, expiration_date)
    with open(f"playlist_cache_{playlist_id}.json", "w") as f:
        json.dump({
            "playlist_id": playlist_cache.playlist_id,
            "latest_episode": playlist_cache.latest_episode,
            "expiration_date": playlist_cache.expiration_date.isoformat()
        }, f)

# Function to check if cache is expired
def is_expired(expiration_date):
    return datetime.now() > datetime.fromisoformat(expiration_date)

# Main function to retrieve the latest episode
def get_latest_episode_from_playlist(playlist_id):
    latest_episode = get_latest_episode(playlist_id)
    # Get the video ID, title, published date
    video_id = latest_episode["id"]
    title = latest_episode["snippet"]["title"]
    published_at = latest_episode["snippet"]["publishedAt"]
    return video_id, title, published_at