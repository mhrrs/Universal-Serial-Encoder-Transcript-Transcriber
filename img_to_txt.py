# create txt file for the data to be labeled 
# use pytesseract to read the pdf into a text file
import enum
from pdf2image import convert_from_path
from pytesseract import image_to_string
import pytesseract
import PyPDF2
import os
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def convert_image_to_text(file):
    text = image_to_string(file)
    return text

folder_path = r'C:\Users\Michael Harris\Desktop\Masters CS\Clemson MSCS\Research\Knijnenburg\transcriptModel\transcript_images'

image_files = os.listdir(folder_path)

# write unlabeled data to training_data file
with open("training_data.txt","w") as file:
    for fname in image_files:
        file_path = os.path.join(folder_path, fname)

        image = Image.open(file_path)

        text = convert_image_to_text(image)

        file.write(text)

print(text)
print(type(text))