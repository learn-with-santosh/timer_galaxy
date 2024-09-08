from config import END_MUSIC, FONT, FONT_SIZE, OUTPUT_END_VIDEOS_PATH, OUTPUT_THUMBNAIL_PATH, OUTPUT_VIDEOS_PATH, TEMPLATE_IMAGE_PATH, TEMPLATE_VIDEO_PATH, TEXT_COLOR, OUTPUT_SIZE, VIDEO_INDEX
from endvideocreator import EndVideoCreator
from thumbnail_generator import ThumbnailGenerator
from video_concatenator import VideoConcatenator
from video_generator import VideoTimerGenerator
from video_splitter import VideoSplitter
from videoprocessor import VideoProcessor

# #generate end video 
# input_video_path = TEMPLATE_VIDEO_PATH + VIDEO_INDEX + ".mp4"
# bg_image_path =  TEMPLATE_IMAGE_PATH  + VIDEO_INDEX +".jpg"
# bg_end_video_path = OUTPUT_END_VIDEOS_PATH + VIDEO_INDEX +"_END.mp4"
# thumbnail_image_path =  OUTPUT_THUMBNAIL_PATH + VIDEO_INDEX

# print("Generating end video...")

# end_video_creator = EndVideoCreator(END_MUSIC, input_video_path, FONT, FONT_SIZE, TEXT_COLOR, OUTPUT_SIZE, bg_end_video_path)
# end_video_creator.create_end_video(overwrite=False)

# durations = [duration * 10 for duration in range(1, 6)]  
# for duration in durations:
#     formatted_text = "{:02d}:{:02d}".format(*divmod(duration, 60))
#     output_path = f"{thumbnail_image_path}-{duration}.jpg"
#     image_adder = ThumbnailGenerator(bg_image_path, output_path, formatted_text)
#     image_adder.add_text_to_image()
    
# durations = [duration * 60 for duration in range(1, 11)]  
# for duration in durations:
#     formatted_text = "{:02d}:{:02d}".format(*divmod(duration, 60))
#     output_path = f"{thumbnail_image_path}-{duration}.jpg"
#     image_adder = ThumbnailGenerator(bg_image_path, output_path, formatted_text)
#     image_adder.add_text_to_image()


# output_temp_video_path = OUTPUT_VIDEOS_PATH  + VIDEO_INDEX+"_temp.mp4"
# final_video= OUTPUT_VIDEOS_PATH  + VIDEO_INDEX+"_10.mp4"

# video_timer_generator = VideoTimerGenerator(input_video_path, output_temp_video_path)
# video_timer_generator.generate_timers(start_time=600, end_time=0, step=-1)


# video_concatenator = VideoConcatenator(bg_end_video_path, output_temp_video_path, final_video)
# video_concatenator.concatenate_videos()

# total_duration = 602
# video_splitter = VideoSplitter(final_video)
# video_splitter.split_interval_videos(total_duration, 10)
# video_splitter.split_segment_videos(total_duration, 60)



if __name__ == "__main__":
    video_index = VIDEO_INDEX
    video_processor = VideoProcessor(video_index)
    video_processor.process_videos()
