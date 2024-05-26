# Image to Text Detector

This Python script uses OpenCV and Pytesseract to detect and extract text from images. It draws bounding boxes around detected text and displays the image with the annotations.

## Prerequisites

Ensure you have the following installed:

- Python 3.x
- OpenCV (`cv2`)
- Pytesseract
- PIL (Pillow)
- Playsound (if using text-to-speech feature)
- Tesseract-OCR

## Installation

1. **Install Python packages**:
    ```sh
    pip install opencv-python pytesseract Pillow playsound
    ```

2. **Install Tesseract-OCR**:
    - Download and install from [here](https://github.com/tesseract-ocr/tesseract).

3. **Set Tesseract path**:
    Ensure the `tesseract_cmd` path in the script points to the Tesseract-OCR executable. Update the path if necessary:
    ```python
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    ```

## Usage

1. **Place your image**:
    - Save your image in the same directory as the script or update the image path in the script:
    ```python
    img = cv2.imread("img1.png")  # Update with your image file
    ```

2. **Run the script**:
    ```sh
    python script_name.py
    ```

3. **View the results**:
    - The script will display the image with detected text highlighted and print the extracted text to the console.
    - Press `q` to close the displayed image.

## Features

- Detects text in images and draws bounding boxes around each word.
- Converts the detected text into a string and prints it.
- Optional: Converts text to speech (commented out in the script).

## Example

```python
import cv2
import pytesseract
from PIL import Image
from playsound import playsound

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = cv2.imread("d2.png")

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img_h, img_w, img_c = img.shape

boxes = pytesseract.image_to_data(img)

sentence = ""

for i, box in enumerate(boxes.splitlines()):
    if i == 0:
        continue
    box = box.split()
    if len(box) == 12:
        x, y, w, h = [int(x) for x in box[6:10]]
        cv2.rectangle(img, (x, y), (x+w, y+h), (157, 84, 33), 1)
        cv2.putText(img, box[11], (x, y+30), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 82, 255), 1)
        sentence += box[11] + " "

cv2.imshow("Image", img)
print(sentence)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
