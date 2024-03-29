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

# Default image path



model = YOLO('../Yolo-Weights/yolov8n.pt')





 

class app:
    def __init__(self):
        self.serialInst = []    
   
    def ai_bottle(self):  
        # self.cap = cv2.VideoCapture(0)
        # self.cap.set(3,1280)
        # self.cap.set(4,720)
        # print("GUI")
        # image_path = './img/automat.png'
        # image2_path = './img/upss.png'
        #         # Load the default image
        # image = Image.open(image_path)
        # image2 = Image.open(image2_path)

        #         # Get the screen size
        # width, height = sg.Window.get_screen_size()

        #         # Resize the image to match the screen size
        # image = image.resize((width, height))
        # image2 = image2.resize((width, height))
        #         # Convert the image to PNG format
        # with io.BytesIO() as bio:
        #     image.save(bio, format="PNG")
        #     data = bio.getvalue()
        # with io.BytesIO() as bio:
        #     image2.save(bio, format="PNG")
        #     data2 = bio.getvalue()

        #         # Create the PySimpleGUI layout
        # layout = [[sg.Image(key='-IMAGE-', size=(width, height), pad=(0,0))]]
        # a=1
        #         # Create the PySimpleGUI window
        # window = sg.Window('Window Title', layout, no_titlebar=True, grab_anywhere=True, finalize=True)
                # Event loop        
        # def open_servo():
        #     if self.serialInst != []:
        #         self.serialInst.write("OPEN".encode('utf-8'))
        #         time.sleep(1)
        #     else:
        #         print("Wysłanie polecenia się nie powiodło")
                
        # def check():
        #     while True:
        #         succes, img = self.cap.read()
        #         results = model(img, stream=True,verbose=False)
        #         for r in results:
        #             boxes = r.boxes
        #             for box in boxes:
        #                 x1,y1,x2,y2=box.xyxy[0]
        #                 # x1,y1, w,h = box.xywh[0]
        #                 # bbox = int(x1),int(y1),int(w),int(h) 
        #                 x1,y1,x2,y2=int(x1),int(y1),int(x2),int(y2)
        #                 # cv2.rectangle(img,(x1,y1),(x2,y2),(0,255,0),2)
        #                 w,h = x2-x1,y2-y1
        #                 conf = math.ceil((box.conf[0]*100))/100
        #                 cls = box.cls[0]
        #                 if(conf >0.2):
        #                     if(int(cls) == 39):
        #                         cmd = "OPEN"
        #                         # cvzone.putTextRect(img,f"Buteleczka{conf}", (max(0,x1),max(35,y1)))
        #                         window['-IMAGE-'].update(data=data)
        #                         open_servo()
        #                         break
        #                     else:
        #                         window['-IMAGE-'].update(data=data2)
        #                         break
        #                         # cvzone.putTextRect(img,f"Nie butelka{conf}", (max(0,x1),max(35,y1)))

        #         cv2.imshow("Image", img)
        #         cv2.waitKey(1)
        # recv = "STA2RT"
        # while True:
        #     print("a")
        #             # Read events
        #     event, values = window.read(timeout=100)
        #     window["-IMAGE-"].update(data=data2)
        #             # Exit loop if window is closed
        #     if event == sg.WIN_CLOSED:
        #             break
        #     if (recv=='START'):
        #         check()
        #     else:
        #         continue

          
            #  if a == 1:
            #         print("q")
            #         window['-IMAGE-'].update(data=data2)
            #  else:
            #         print("h")
            #         window['-IMAGE-'].update(data=data)
            #  a = sg.popup_get_text('Podaj liczbe:', default_text='', no_titlebar=True, grab_anywhere=True)
            #  print("a:",a)
                # Close the PySimpleGUI window
        # window.close()
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
           
            def name():
                    window["-IMAGE-"].update(data=data)

            #         cv2.waitKey(1)
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
            window.close()

                
    #  if a == 1:
    #         print("q")
    #         window['-IMAGE-'].update(data=data2)
    #  else:
    #         print("h")
    #         window['-IMAGE-'].update(data=data)
    #  a = sg.popup_get_text('Podaj liczbe:', default_text='', no_titlebar=True, grab_anywhere=True)
    #  print("a:",a)
        # Close the PySimpleGUI window

    def ino(self):
        ports = serial.tools.list_ports.comports()
        
        self.serialInst = serial.Serial()

        portsList =[]

        for onePort in ports:
            portsList.append(str(onePort))
            print(str(onePort))
        val = input("Select Port: COM")

        for x in range(0,len(portsList)):
            if portsList[x].startswith("COM" + str(val)):
                portVar = "COM" + str(val)
                print(portVar)
        
        self.serialInst.baudrate = 115200
        self.serialInst.port = portVar
        self.serialInst.timeout = 1
        self.serialInst.open()
    def cmd_ino(self):
        if self.serialInst:
            while True:
                try:
                    cmd = input("Arduino command: ")
                    self.serialInst.write(cmd.encode('utf'))
                    packet = self.serialInst.readline()
                    print(packet.decode('utf'))
                    if cmd == 'exit':
                        exit()
                except UnicodeDecodeError:
                    print("Error: received unexpected data from serial port")
        else:
            self.run()
    def run(self):
        menu_options = {
            1:"Otwórz port",
            2:"Uruchom AI",
            3:"Wyślij komende do arduino",
            4:"Uruchom GUI",
            5:"EXIT"
        }
        def print_menu():
            for key in menu_options.keys():
                print (key, '--', menu_options[key] )
            option = int(input('Enter your choice: ')) 
            if option == 1:
                print('Wybrano opcje \'Option 1\'')
                self.ino()
            elif option == 2:
                print('Wybrano opcje \'Option 2\'')
                self.ai_bottle()
            elif option == 3:
                self.cmd_ino()
            elif option == 4:
                self.gui()
            elif option == 5:
                exit()
            else:
                print('Invalid option. Please enter a number between 1 and 3.')
        while True:
            print_menu()

if __name__ =="__main__":
    app = app()
    app.run()
