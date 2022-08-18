from PIL import ImageGrab
from pytesseract import pytesseract
import pyautogui
import time
import PySimpleGUI as sg
import os




def auto():
    try:
        # Add some color
        # to the window
        sg.theme('DarkBlack')

        # Very basic window.
        # Return values using
        # automatic-numbered keys

        layout1 = [
        [sg.Text(r"            Hit 'Start' to perform searches    ")],
        [sg.Text('Search Engine ', size=(15, 1)), sg.InputText(size=(20, 1))],
        #[sg.Text("                             ")],
        [sg.Button("Start",size=(36,1))]
         ]

        window1 = sg.Window('Searchify', layout1)
        while True:
            # simple loop to update the values
            event1, values1 = window1.read()
            global url
            url = values1[0]

            if url == "":
                break

            if event1 == sg.WIN_CLOSED:
                break

            if event1 == "Start":
                flash()


        window1.close()

    except:
        pass



def flash():

    # Defining paths to tesseract.exe
    path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    pyautogui.hotkey('super', 'shift', 's')
    time.sleep(7)

    image_grab = ImageGrab.grabclipboard()  # images passed from the clipboard


    # Providing the tesseract
    # executable location to pytesseract library
    pytesseract.tesseract_cmd = path_to_tesseract

    # Passing the image object to
    # image_to_string() function
    # This function will
    # extract the text from the image
    text = pytesseract.image_to_string(image_grab)

    # Displaying the extracted text
    print(text[:-1])

    os.system('cmd /c start http://www.' + str(url))
    time.sleep(4)
    pyautogui.write(text[:-1])
    pyautogui.press('enter')




auto()

