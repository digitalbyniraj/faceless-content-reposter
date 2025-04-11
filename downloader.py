from pytube import YouTube
from pathlib import Path
import os

def download_youtube_video(url, save_path='downloads'):
    Path(save_path).mkdir(parents=True, exist_ok=True)
    yt = YouTube(url)
    stream = yt.streams.filter(file_extension='mp4').get_highest_resolution()
    filename = yt.title.replace(" ", "_") + ".mp4"
    stream.download(output_path=save_path, filename=filename)
    return os.path.join(save_path, filename)
