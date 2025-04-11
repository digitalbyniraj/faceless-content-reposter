from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import os

def add_watermark(video_path, watermark_text="YourChannel", output_folder="watermarked"):
    os.makedirs(output_folder, exist_ok=True)
    clip = VideoFileClip(video_path)
    watermark = TextClip(watermark_text, fontsize=24, color='white', font="Arial-Bold")\
        .set_position(("right", "bottom"))\
        .set_duration(clip.duration)

    final = CompositeVideoClip([clip, watermark])
    output_path = os.path.join(output_folder, os.path.basename(video_path))
    final.write_videofile(output_path, codec='libx264', audio_codec='aac')
    return output_path
