import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = Image.open("img1.png")

# text = pytesseract.image_to_string(img)
# print(text)
# text = pytesseract.image_to_boxes(img)
# print(text)
text = pytesseract.image_to_data(img)
print(text)