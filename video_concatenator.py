import os
from moviepy.editor import VideoFileClip, concatenate_videoclips

from config import FPS, VIDEO_CODEC

class VideoConcatenator:
    def __init__(self, video1_path, video2_path, output_path):
        self.video1_path = video1_path
        self.video2_path = video2_path
        self.output_path = output_path
    
    def check_file_exists(self):
        return os.path.exists(self.output_path)
    
    def concatenate_videos(self,overwrite=False):
        if not overwrite and self.check_file_exists():
            print(f"File {self.output_path} already exists. Operation canceled.")
            return
        
        # Load the video clips
        video1 = VideoFileClip(self.video1_path)
        video2 = VideoFileClip(self.video2_path)

        # Concatenate the video clips
        final_clip = concatenate_videoclips([video2, video1])

        # Write the result to a file
        final_clip.write_videofile(self.output_path, codec=VIDEO_CODEC, fps=FPS)

        # Close the video clips
        video1.close()
        video2.close()
