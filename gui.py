# import PySimpleGUI as sg
# from PIL import Image
# import io

# # Załaduj obraz
# image = Image.open('./img/automat.png')

# # Zmień rozmiar obrazka na rozmiar ekranu
# width, height = sg.Window.get_screen_size()
# image = image.resize((width, height))

# # Konwertuj obrazek na format PNG
# with io.BytesIO() as bio:
#     image.save(bio, format="PNG")
#     data = bio.getvalue()

# # Stwórz układ i okno PySimpleGUI
# layout = [[sg.Image(data=data, size=(width, height), pad=(0,0))]]

# # Ustaw parametry okna PySimpleGUI
# window = sg.Window('Window Title', layout, no_titlebar=True, grab_anywhere=True)

# # Pętla zdarzeńa
# while True:
#     event, values = window.read()
#     if event == sg.WIN_CLOSED:
#         break

# # Zamknij okno
# window.close()










from ultralytics import YOLO
import cv2
import cvzone
import math
import serial.tools.list_ports
import time
# Load model
import PySimpleGUI as sg
from PIL import Image
import io
model = YOLO('../Yolo-Weights/yolov8n.pt')

#  # self.cap.set(4,720)]
cap = cv2.VideoCapture(0)
cap.set(3,720)
cap.set(4,480)
print("GUI")
image_path = './img/automat.png'
image2_path = './img/upss.png'
        # Load the default image
image = Image.open(image_path)
image2 = Image.open(image2_path)

        # Get the screen size
width, height = sg.Window.get_screen_size()

        # Resize the image to match the screen size
image = image.resize((width, height))
image2 = image2.resize((width, height))
        # Convert the image to PNG format
with io.BytesIO() as bio:
    image.save(bio, format="PNG")
    data = bio.getvalue()
with io.BytesIO() as bio:
    image2.save(bio, format="PNG")
    data2 = bio.getvalue()

        # Create the PySimpleGUI layout
layout = [[sg.Image(key='-IMAGE-', size=(width, height), pad=(0,0))]]
a=1
        # Create the PySimpleGUI window
window = sg.Window('Window Title', layout, no_titlebar=True, grab_anywhere=True, finalize=True)
        # Event loop        
# def open_servo():
#     if serialInst != []:
#         serialInst.write("OPEN".encode('utf-8'))
#         time.sleep(1)
#     else:
#         print("Wysłanie polecenia się nie powiodło")
        
def check():
        succes, img = cap.read()
        results = model(img, stream=True,verbose=False)
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1,y1,x2,y2=box.xyxy[0]
                # x1,y1, w,h = box.xywh[0]
                # bbox = int(x1),int(y1),int(w),int(h) 
                x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2)
                # cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
                w,h = x2-x1,y2-y1
                conf = math.ceil((box.conf[0]*100))/100
                cls = box.cls[0]
                if(conf >0.2):
                    if(int(cls) == 39):
                        cmd = "OPEN"
                        # cvzone.putTextRect(img,f"Buteleczka{conf}", (max(0,x1),max(35,y1)))
                        window['-IMAGE-'].update(data=data)
                        break
                    else:
                        window['-IMAGE-'].update(data=data2)
                        break
                        # cvzone.putTextRect(img,f"Nie butelka{conf}", (max(0,x1),max(35,y1)))

        cv2.imshow("Image", img)
def name():
         window["-IMAGE-"].update(data=data)

recv = "START"
while True:
    print("a")
            # Read events
    event, values = window.read(timeout=100)
    window["-IMAGE-"].update(data=data2)
            # Exit loop if window is closed
    if event == sg.WIN_CLOSED:
            break
    if (recv=='START'):
        name()
    else:
        continue

    
    #  if a == 1:
    #         print("q")
    #         window['-IMAGE-'].update(data=data2)
    #  else:
    #         print("h")
    #         window['-IMAGE-'].update(data=data)
    #  a = sg.popup_get_text('Podaj liczbe:', default_text='', no_titlebar=True, grab_anywhere=True)
    #  print("a:",a)
        # Close the PySimpleGUI window
window.close()