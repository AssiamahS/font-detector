import cv2
import pytesseract
from fontTools.ttLib import TTFont
import os

# Function to extract text from an image
def extract_text(image_path):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)
    return text

# Function to recognize font from text
def recognize_font(text):
    fonts_path = '/path/to/fonts/directory'  # Directory containing font files (.ttf, .otf)
    text_fonts = []
    for font_file in os.listdir(fonts_path):
        font_path = os.path.join(fonts_path, font_file)
        font = TTFont(font_path)
        if text in font.getGlyphNames():
            text_fonts.append(font_file)
    return text_fonts

if __name__ == "__main__":
    image_path = 'path_to_your_image_file.jpg'  # Path to your image file
    text = extract_text(image_path)
    print("Extracted Text:", text)
    fonts = recognize_font(text)
    print("Possible Fonts:", fonts)
