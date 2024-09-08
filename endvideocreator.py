import os
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip, AudioFileClip
from config import AUDIO_CODEC, TEXT_POSITION, VIDEO_CODEC, FPS, THREADS

class EndVideoCreator:
    def __init__(self, end_music, bg_end_video, font, font_size, text_color, output_size, output_path):
        self.end_music = end_music
        self.bg_end_video = bg_end_video
        self.font = font
        self.font_size = font_size
        self.text_color = text_color
        self.output_size = output_size
        self.output_path = output_path

    def create_timer_text(self, minutes, seconds):
        return "{:02d}:{:02d}".format(int(minutes), int(seconds))

    def check_file_exists(self):
        return os.path.exists(self.output_path)
    
    def create_end_video(self, overwrite=False):
        if not overwrite and self.check_file_exists():
            print(f"File {self.output_path} already exists. Operation canceled.")
            return
        if TEXT_POSITION is None:
            text_position = ('center', 'center')
        else:
            text_position = TEXT_POSITION     
            
        print(text_position)     
            
        timer_text = self.create_timer_text(0, 0)
        # text_position= (60,-20)
        audio_clip = AudioFileClip(self.end_music)
        bg_video = VideoFileClip(self.bg_end_video).subclip(0, audio_clip.duration)

        txt_clip = TextClip(timer_text, fontsize=self.font_size, font=self.font, color=self.text_color, size=self.output_size)
        
        # Calculate the position of the text
        text_width = txt_clip.w
        text_height = txt_clip.h
        x = (bg_video.w - text_width) / 2
        y = (bg_video.h - text_height) / 2

        final_clip = CompositeVideoClip([bg_video, txt_clip.set_pos((x,y)).set_duration(audio_clip.duration)])
        final_clip = final_clip.set_audio(audio_clip)

        final_clip.write_videofile(self.output_path, codec=VIDEO_CODEC, audio_codec=AUDIO_CODEC, fps=FPS, threads=THREADS)
