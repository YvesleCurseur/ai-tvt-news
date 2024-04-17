# Note: was in a bit rush it's why there is so many print statements, will clean it later
import os
import models
from datetime import datetime
from database import SessionLocal

# Function import
from core.generate_summary import generate_spr
from core.download_transcript import get_transcript_from_video
from core.get_last_video_infos import get_latest_episode_from_playlist

db = SessionLocal()

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

PLAYLIST_ID = os.getenv("YOUTUBE_PLAYLIST_ID")

# First get the last video from the playlist

async def get_last_video_and_transcript():
    # Get all the previous news
    print("==========")
    print("Getting all previous news...")
    news = db.query(models.News).order_by(models.News.created_at.desc()).all()
    print("==========")
    print("Getting last video infos...")
    video_id, title, published_at = get_latest_episode_from_playlist(PLAYLIST_ID)
    # Check if there is already a news with the same video_id
    news_with_same_video_id = [n for n in news if n.video_id == video_id]
    if news_with_same_video_id:
        print(news_with_same_video_id[0])
        print("News already exists for this video ID!")
        # Remove the playlist cache
        print("==========")
        print("Removing playlist cache...")
        os.remove("playlist_cache_PLZsG-wdeIZJV1eM3yur5AEDssh_rs5wFD.json")
        return news_with_same_video_id[0]
    else:
        print("News does not exist for this video ID!")
        # print with a template string
        print(f" The title was : {title} \n Youtube Video url: https://www.youtube.com/watch?v={video_id} \n Published at: {published_at}")
        print("==========")
        print("Getting transcript from last video...")
        # Get the transcript
        transcript = get_transcript_from_video(video_id, title)
        if not transcript:
            print("==========")
            print("Removing playlist cache...")
            os.remove("playlist_cache_PLZsG-wdeIZJV1eM3yur5AEDssh_rs5wFD.json")
            return "Pas de transcription disponible pour cette vidéo."
        else:
            description = ""
            print("Transcript downloaded !")
            print("==========")
            print("Generating News...")
            transcript = generate_spr()
            print("==========")
            print("That's it for today, enjoy ! 🎉")
            # creating a new data
            print("==========")
            print("Saving news to database...")
            # Save the news
            published_at_datetime = datetime.strptime(published_at, '%Y-%m-%dT%H:%M:%SZ')
            new = models.News(title=title, video_id=video_id, transcript=transcript, description=description, published_at=published_at_datetime)
            db.add(new)
            db.commit()
            print("News saved !", new)
            # Remove the playlist cache
            print("==========")
            print("Removing playlist cache...")
            os.remove("playlist_cache_PLZsG-wdeIZJV1eM3yur5AEDssh_rs5wFD.json")
            return new
