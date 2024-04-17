import os
from youtube_transcript_api import YouTubeTranscriptApi
from .get_last_video_infos import get_latest_episode_from_playlist

directory = os.path.dirname(__file__)
playlist_id = os.getenv("YOUTUBE_PLAYLIST_ID")

def save_file(filepath, content):
    directory = os.path.dirname(filepath)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(filepath, 'w', encoding='utf-8') as outfile:
        outfile.write(content)

def clean_title(title):
    contraband = [':','/','\\','?','"']
    for c in contraband:
        title = title.replace(c,'')
    return title

# Get the latest video from the playlist
video_id, title, published_at = get_latest_episode_from_playlist(playlist_id)

# Make a fucntion transcript for the latest video
def get_transcript_from_video(video_id, title):
    block = ''  # Initialize block to an empty string
    if video_id:
        try:
            # Get the transcript for the video
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['fr', 'en'])
            text = [i['text'] for i in transcript]
            block = ' '.join(text)
            title = clean_title(title)
            save_file('core/transcripts/%s.txt' % title, block)
        except Exception as oops:
            # Convert the exception to a string
            error_message = str(oops)
            save_file('core/transcripts/%s.txt' % title, error_message)
    return block




