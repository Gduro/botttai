import threading
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
# Define a function to update the window image in a separate thread
image_path = './img/automat.png'
image2_path = './img/upss.png'
image = Image.open(image_path)
image2 = Image.open(image2_path)
width, height = sg.Window.get_screen_size()
image = image.resize((width, height))
image2 = image2.resize((width, height))
with io.BytesIO() as bio:
    image.save(bio, format="PNG")
    data = bio.getvalue()
with io.BytesIO() as bio:
    image2.save(bio, format="PNG")
    data2 = bio.getvalue()

def update_image(window):
    # Load the YOLO model
    model = YOLO('../Yolo-Weights/yolov8n.pt')

    # Open the video capture device
    cap = cv2.VideoCapture(0)
    cap.set(3, 720)
    cap.set(4, 480)

    # Load the images

    # Loop to continuously update the image on the window
    while True:
        # Read a frame from the video stream
        succes, img = cap.read()

        # Run the YOLO model on the frame to detect objects
        results = model(img, stream=True, verbose=False)

        # Loop over the detected objects and update the window image accordingly
        for r in results:
            boxes = r.boxes
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
                w, h = x2 - x1, y2 - y1
                conf = math.ceil((box.conf[0] * 100)) / 100
                cls = box.cls[0]
                if conf > 0.2:
                    if int(cls) == 39:
                        window['-IMAGE-'].update(data=data2)
                        time.sleep(2)
                        window['-IMAGE-'].update(data=data)
                        break
                    else:
                        break

        # Display the image in a window
        cv2.imshow("Image", img)
        cv2.waitKey(1)

# Create the PySimpleGUI window
layout = [[sg.Image(key='-IMAGE-', size=(width, height), pad=(0, 0))]]
window = sg.Window('Window Title', layout, no_titlebar=True, grab_anywhere=True, finalize=True)
window['-IMAGE-'].update(data=data)
# Create a thread to update the window image
thread = threading.Thread(target=update_image, args=(window,))
thread.start()

# Event loop for the GUI
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

# Wait for the image update thread to finish
thread.join()

# Close the PySimpleGUI window
window.close()
