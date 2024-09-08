from moviepy.editor import VideoFileClip

from config import AUDIO_CODEC, OUTPUT_VIDEOS_PATH, VIDEO_CODEC,VIDEO_INDEX

class VideoSplitter:
    def __init__(self, input_video_path):
        self.input_video_path = input_video_path

    def split_video(self, output_path, start_time, end_time):
        clip = VideoFileClip(self.input_video_path).subclip(start_time, end_time)
        clip.write_videofile(output_path, codec=VIDEO_CODEC, audio_codec=AUDIO_CODEC)
        clip.close()

    def split_interval_videos(self, total_duration, interval_duration):
        for i in range(int(560 / interval_duration), int(total_duration / interval_duration) + 1):
            start_time = (i - 1) * interval_duration
            end_time = total_duration
            output_path = f"{OUTPUT_VIDEOS_PATH}{VIDEO_INDEX}_{600-start_time}s.mp4"
            self.split_video(output_path, start_time, end_time)

    def split_segment_videos(self, total_duration, segment_duration):
        for i in range(2, int(total_duration / segment_duration) + 1):
            start_time = (i - 1) * segment_duration
            end_time = total_duration
            output_path = f"{OUTPUT_VIDEOS_PATH}{VIDEO_INDEX}_{11-i}s.mp4"
            self.split_video(output_path, start_time, end_time)

# Example usage
if __name__ == "__main__":
    input_video_path = "data/output/video/timers/BG10_10.mp4"
    output_video_prefix = "BG10_"
    total_duration = 602  # 10 minutes in seconds

    video_splitter = VideoSplitter(input_video_path, output_video_prefix)
    video_splitter.split_interval_videos(total_duration, 10)
    video_splitter.split_segment_videos(total_duration, 60)
