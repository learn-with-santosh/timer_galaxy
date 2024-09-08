from PIL import Image, ImageDraw, ImageFont

from config import FONT, FONT_SIZE, OUTPUT_SIZE, TEXT_COLOR, TEXT_POSITION

class ThumbnailGenerator:
    def __init__(self, input_image_path, output_image_path, text, **kwargs):
        self.input_image_path = input_image_path
        self.output_image_path = output_image_path
        self.text = text
        self.kwargs = kwargs

    def open_image(self):
        return Image.open(self.input_image_path)

    def create_output_image(self):
        # size = self.kwargs.get('output_size', OUTPUT_SIZE)
        return Image.new("RGB", OUTPUT_SIZE, color=(255, 255, 255))

    def paste_image(self, original_image, position, output_image):
        output_image.paste(original_image, position)

    def create_text_draw(self, output_image):
        return ImageDraw.Draw(output_image)

    def load_font(self):
        # font_path = self.kwargs.get('font_path', FONT)
        # font_size = self.kwargs.get('font_size', FONT_SIZE)
        return ImageFont.truetype(FONT, FONT_SIZE)

    def calculate_text_position(self, output_size, text_width, text_height):
        return ((output_size[0] - text_width) // 2, (output_size[1] - text_height) // 2)

    def add_text(self, draw, text, font, text_position):
        text_color = self.kwargs.get('text_color', TEXT_COLOR)
        draw.text(text_position, text, font=font, fill=text_color)

    def save_image(self, output_image):
        output_image.save(self.output_image_path)
        print(f"File '{self.output_image_path}' created.")


    def add_text_to_image(self):
        original_image = self.open_image()
        output_image = self.create_output_image()
        position = ((OUTPUT_SIZE[0] - original_image.width) // 2, (OUTPUT_SIZE[1] - original_image.height) // 2)
        self.paste_image(original_image, position, output_image)
        draw = self.create_text_draw(output_image)
        font = self.load_font()
        text_width, text_height = draw.textsize(self.text, font)
        print(OUTPUT_SIZE,text_width, text_height)
        if TEXT_POSITION is None :
            text_position = self.calculate_text_position(OUTPUT_SIZE, text_width, text_height)
            #text_position = ((original_image.width - text_width) // 2, (original_image.height - text_height) // 2)

        else :
            text_position = TEXT_POSITION
        
        print(text_position)
        
        self.add_text(draw, self.text, font, text_position)
        self.save_image(output_image)

