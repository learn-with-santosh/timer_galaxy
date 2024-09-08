import os
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
from config import FONT, FONT_SIZE, OUTPUT_SIZE, TEXT_COLOR, TEXT_POSITION

class VideoTimerGenerator:
    def __init__(self, background_video_path, output_video_path):
        self.background_video_path = background_video_path
        self.output_video_path = output_video_path
        self.out_width, self.out_height = OUTPUT_SIZE

        self.clip_list = [VideoFileClip(background_video_path).subclip(0,600)]
        self.start_time = 0

    def format_timer(self, seconds):
        minutes, seconds = divmod(seconds, 60)
        return "{:02d}:{:02d}".format(int(minutes), int(seconds))
    
    def check_file_exists(self):
        return os.path.exists(self.output_video_path)
    
    def add_timer_clip(self, time):
        timer_text = self.format_timer(time)
        if TEXT_POSITION is None:
            text_position = ('center', 'center')
        else:
            text_position = TEXT_POSITION          
        
        text_position= (60,-20)

        timer_clip = TextClip(timer_text, font=FONT, fontsize=FONT_SIZE, color=TEXT_COLOR,
                              bg_color="transparent", align='Center', size=(self.out_width, self.out_height))
        timer_clip = timer_clip.set_position(text_position).set_duration(1.0).set_start(self.start_time)
        self.start_time += 1
        self.clip_list.append(timer_clip)

    def generate_timers(self, start_time=180, end_time=119, step=-1,overwrite=False):
        if not overwrite and self.check_file_exists():
            print(f"File {self.output_video_path} already exists. Operation canceled.")
            return
        
        for time in range(start_time, end_time, step):
            self.add_timer_clip(time)

        final_clip = CompositeVideoClip(self.clip_list)
        final_clip = final_clip.resize(newsize=(self.out_width, self.out_height))
        final_clip.write_videofile(self.output_video_path)