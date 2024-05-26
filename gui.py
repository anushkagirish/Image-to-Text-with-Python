import cv2
import pytesseract
from PIL import Image
from gtts import gTTS
from playsound import playsound
from tkinter import*


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = cv2.imread("img1.png")  # to read image

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

sentence=""


for i, box in enumerate(boxes.splitlines()):
    #print(box)
    if i == 0:
        continue
    
    box = box.split()
    #print(box)

    if len(box)==12:
         x, y, w, h = [int(x) for x in box[6:10]]
         #print(x, y, w, h)

         cv2.rectangle(img, (x,y), (x+w, y+h),(0,0,255),1)

         cv2.putText(img, box[11], (x, y+30), cv2.FONT_HERSHEY_COMPLEX, 0.5,(0,0,255),1)
         
         sentence += box[11]+" "

         
def onSubmitButtonClicked():
     cv2.imshow("Image",img)  #to open image
     #print(sentence)
     sentence2 =Entry(root,textvariable = sentence)
     print(sentence2)
    

def onClearButtonClicked():
    sound = gTTS(text = sentence, lang= 'en')
    sound.save("sound1.mp3")
    playsound("sound1.mp3")
    

def onExitButtonClicked():
      root.destroy()

root=Tk()
root.title("My First GUI Application")
root.geometry("%dx%d+0+0"%(400,250))

bootcampMessage=Label(text ="Image to text n speech <3")
bootcampMessage.pack()
todaysTopic=Label(text=" ")
todaysTopic.pack()

#Taking in values in the form
nameLabel=Label(text = "Text from image: ")
nameLabel.place(x=20,y=50)

daysAttended=Label(text= "Audio :")
daysAttended.place(x=20,y=70)

#Taking in values from the user
nameString=StringVar()
nameEntry =Entry(root,textvariable = nameString)
nameEntry.place(x=240,y=50)

daysAttendedString=StringVar()
daysAttendedEntry=Entry(root,textvariable= daysAttendedString)
daysAttendedEntry.place(x=240,y=70)

resultString=StringVar()
result=Entry(root,textvariable=resultString,width=50).place(x=40,y=100)

#Placing buttons
submitButton=Button(text ="to text",command=onSubmitButtonClicked)
submitButton.place(x=100,y=150)
clearButton=Button(text="to audio",command=onSubmitButtonClicked)
clearButton.place(x=150,y=150)
exitButton=Button(text="Exit", command=onExitButtonClicked)
exitButton.place(x=190,y=150)
root.mainloop()