import cv2
import pytesseract
from PIL import Image
#from gtts import gTTS
from playsound import playsound

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = cv2.imread("d2.png")  # to read image

img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)    # to convert into rgb

# cv2.imshow("Image",img)  #to open image

img_h, img_w, img_c = img.shape     #shape of image

# boxes = pytesseract.image_to_boxes(img)

# for box in boxes.splitlines():
#     box = box.split(" ")
#     #print(box)

#     x, y, w, h = [int(x) for x in box[1:5]]
#     #print(x,y,w,h)

#     cv2.rectangle(img, (x, img_h -y), (w, img_h -h),(0,0,255),1)

#     cv2.putText(img, box[0] , (x, img_h - y +10), cv2.FONT_HERSHEY_COMPLEX, 0.5,(0,0,255),1)


boxes = pytesseract.image_to_data(img)

sentence = ""

for i, box in enumerate(boxes.splitlines()):
    #print(box)
    if i == 0:
        continue
    
    box = box.split()
    #print(box)

    if len(box)==12:
         x, y, w, h = [int(x) for x in box[6:10]]
         #print(x, y, w, h)

         cv2.rectangle(img, (x,y), (x+w, y+h),(157,84,33),1)

         cv2.putText(img, box[11], (x, y+30), cv2.FONT_HERSHEY_COMPLEX, 0.5,(0,82,255),1)
         
         sentence += box[11]+" "

cv2.imshow("Image",img)  #to open image
print(sentence)

#text to sound
#sound = gTTS(text = sentence, lang= 'en')
#sound.save("sound.mp3")
#playsound("sound.mp3")


#exit
if cv2.waitKey(0) & 0XFF == ord('q') : #to close image if q is pressed
    cv2.destroyAllWindows()
