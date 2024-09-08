# from PIL import Image, ImageDraw, ImageFont

# def add_text_to_image(input_image_path, text, output_image_path, output_size=(1920, 1080), 
#                       font_path="fonts/Wedges.ttf", font_size=400, text_color="#ffffff"):
#     original_image = Image.open(input_image_path)
#     output_image = Image.new("RGB", output_size, color=(255, 255, 255))
#     position = ((output_size[0] - original_image.width) // 2, (output_size[1] - original_image.height) // 2)
#     output_image.paste(original_image, position)
#     draw = ImageDraw.Draw(output_image)
#     font = ImageFont.truetype(font_path, font_size)
#     text_width, text_height = draw.textsize(text, font)
#     text_position = ((output_size[0] - text_width) // 2, (output_size[1] - text_height) // 2)
#     # X= output_size[0] - text_width-100
#     # Y=200
#     #text_position = (350,550)

#     draw.text(text_position, text, font=font, fill=text_color)
#     output_image.save(output_image_path)

# # durations = [90]  # Add more durations as needed
# #durations = [duration * 10 for duration in range(1, 11)]  # 1 minute to 1 hour, 1-minute intervals
# durations = [duration * 60 for duration in range(1, 11)]  # 1 minute to 1 hour, 1-minute intervals

# # Example usage in a loop
# for duration in durations:
#     formatted_text = "{:02d}:{:02d}".format(*divmod(duration, 60))
#     output_path = f"output/thumbnail/BG14-{duration}.jpg"
#     add_text_to_image("templates/images/BG14.jpg", formatted_text, output_path, output_size=(1920, 1080))



from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip,AudioFileClip

END_MUSIC = "music/End.mp3"
BG_END_VIDEO = "templates/videos/BG14.mp4"
FONT = "fonts/Wedges.ttf"
FONT_SIZE = 400
TEXT_COLOR = "#ffffff"
OUTPUT_SIZE = (1920, 1080)
output_path = 'templates/BG14_END.mp4'



timer_text = "{:02d}:{:02d}".format(int(0), int(0))
audio_clip = AudioFileClip(END_MUSIC)   
BG_VIDEO = VideoFileClip(BG_END_VIDEO).subclip(0, audio_clip.duration)

txt_clip = TextClip(timer_text, fontsize=FONT_SIZE, font=FONT, color=TEXT_COLOR, size=OUTPUT_SIZE)
text_position =('center', 'center')
#text_position =(-50,230)
final_clip = CompositeVideoClip([BG_VIDEO,txt_clip.set_pos(text_position).set_duration(audio_clip.duration)])
final_clip = final_clip.set_audio(audio_clip)
final_clip.write_videofile(output_path,codec='libx264', audio_codec='aac', fps=30, threads=6)