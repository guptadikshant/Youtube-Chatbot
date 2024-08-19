import os
import shutil

import whisper
from yt_dlp import YoutubeDL


def download_youtube_video_transcript(video_link: str, path: str) -> None:
    YOUTUBE_DIR = "youtube_videos"
    try:
        os.makedirs(YOUTUBE_DIR, exist_ok=True)
        
        URLS = [video_link]
    
        ydl_opts = {
            'format': 'm4a/bestaudio/best',
            'postprocessors': [{  # Extract audio using ffmpeg
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',  # file will be saved into mp3 format
            }],
            # '%(ext)s': Automatically replaces itself with the appropriate file extension (like mp3, m4a, wav) 
            # based on the downloaded content.
            'outtmpl': os.path.join(YOUTUBE_DIR, f'{"desired_filename"}.%(ext)s')
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download(URLS)

        whisper_model = whisper.load_model("base")
    
        file = os.listdir(YOUTUBE_DIR)[0]
        
        audio_file_path = os.path.join(YOUTUBE_DIR, file)
        
        print(f"Audio file location: {audio_file_path}")
    
        transcription = whisper_model.transcribe(audio_file_path)["text"].strip()
    
        with open(os.path.join(path, "transcript.txt"), "w") as file:
            file.write(transcription)
    
    except FileNotFoundError:
        print(f"{os.path.join(path, 'transcript.txt')} already exists")
    
    finally:
        shutil.rmtree(YOUTUBE_DIR)
