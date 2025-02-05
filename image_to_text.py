import cv2
import pytesseract
from pytesseract import Output
from PIL import Image

# Provide the image path where your image is located
image_path = 'YOUR_IMAGE_PATH'

# Load the image
img = cv2.imread(image_path)

# Use pytesseract to extract text from the image
extracted_text = pytesseract.image_to_string(img)

# Print the extracted text
print(extracted_text)
