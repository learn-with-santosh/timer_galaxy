from config import END_MUSIC, FONT, FONT_SIZE, OUTPUT_END_VIDEOS_PATH, OUTPUT_THUMBNAIL_PATH, OUTPUT_VIDEOS_PATH, TEMPLATE_IMAGE_PATH, TEMPLATE_VIDEO_PATH, TEXT_COLOR, OUTPUT_SIZE, VIDEO_INDEX
from endvideocreator import EndVideoCreator
from thumbnail_generator import ThumbnailGenerator
from video_concatenator import VideoConcatenator
from video_generator import VideoTimerGenerator
from video_splitter import VideoSplitter

class VideoProcessor:
    def __init__(self, video_index):
        self.video_index = video_index
        self.template_video_path = TEMPLATE_VIDEO_PATH + video_index + ".mp4"
        self.bg_image_path = TEMPLATE_IMAGE_PATH + video_index + ".jpg"
        self.bg_end_video_path = OUTPUT_END_VIDEOS_PATH + video_index + "_END.mp4"
        self.thumbnail_image_path = OUTPUT_THUMBNAIL_PATH + video_index
        self.output_temp_video_path = OUTPUT_VIDEOS_PATH + video_index + "_temp.mp4"
        self.final_video = OUTPUT_VIDEOS_PATH + video_index + "_10.mp4"
        self.total_duration = 602

    def process_end_video(self):
        print("Generating end video...")
        end_video_creator = EndVideoCreator(END_MUSIC, self.template_video_path, FONT, FONT_SIZE, TEXT_COLOR, OUTPUT_SIZE, self.bg_end_video_path)
        end_video_creator.create_end_video(overwrite=True)
        print("End video generation completed.")


    def generate_thumbnails(self):
        print("Generating thumbnails...")
        durations = [duration * 10 for duration in range(1, 6)]  
        for duration in durations:
            formatted_text = "{:02d}:{:02d}".format(*divmod(duration, 60))
            output_path = f"{self.thumbnail_image_path}-{duration}.jpg"
            image_adder = ThumbnailGenerator(self.bg_image_path, output_path, formatted_text)
            image_adder.add_text_to_image()

        durations = [duration * 60 for duration in range(1, 11)]  
        for duration in durations:
            formatted_text = "{:02d}:{:02d}".format(*divmod(duration, 60))
            output_path = f"{self.thumbnail_image_path}-{duration}.jpg"
            image_adder = ThumbnailGenerator(self.bg_image_path, output_path, formatted_text)
            image_adder.add_text_to_image()
            
        print("Thumbnail generation completed.")


    def generate_temp_video(self):
        print("Generating video timer...")
        video_timer_generator = VideoTimerGenerator(self.template_video_path, self.output_temp_video_path)
        video_timer_generator.generate_timers(start_time=600, end_time=0, step=-1)
        print("Video timer generation completed.")


    def concatenate_videos(self):
        print("Concatenating videos...")
        video_concatenator = VideoConcatenator(self.bg_end_video_path, self.output_temp_video_path, self.final_video)
        video_concatenator.concatenate_videos()
        print("Video concatenation completed.")


    def split_videos(self):
        print("Splitting videos...")
        video_splitter = VideoSplitter(self.final_video)
        video_splitter.split_interval_videos(self.total_duration, 10)
        video_splitter.split_segment_videos(self.total_duration, 60)
        print("Video splitting completed.")


    def process_videos(self):
        # self.process_end_video()
        # self.generate_thumbnails()
        self.generate_temp_video()
        self.concatenate_videos()
        self.split_videos()

# if __name__ == "__main__":
#     video_index = VIDEO_INDEX
#     video_processor = VideoProcessor(video_index)
#     video_processor.process_videos()
