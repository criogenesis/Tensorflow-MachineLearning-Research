'''
Created on May 4, 2019
@author: Zack
'''
#-- include('examples/showgrabfullscreen.py') --#
from PIL import ImageGrab
from PIL import Image
import time
import win32gui
import winsound
from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()


NumberOfScreenshots = int(input("How many Screenshots would " +
                                "you like taken?:\n"))

count = 1

screenDecision = input(
    "Type 1 for cursor\n2 for captcha\n3 for chrome icon\n" +
    "4 for edge icon\nor 5 for normal screenshot: \n")

toggle = True
time.sleep(5)
winsound.PlaySound('sound.wav', winsound.SND_FILENAME)

while(count <= NumberOfScreenshots):
    if screenDecision == "1":
        im = ImageGrab.grab()
        cursor = Image.open('cursor.png')

        curX, curY = win32gui.GetCursorPos()
        im.paste(cursor, box=(curX, curY), mask=cursor)

        fileName = "cursorTest%d.png" % count
        print(fileName)
        im.save(fileName, "PNG")
    if screenDecision == "2":
        im = ImageGrab.grab()
        if toggle is True:
            captcha = Image.open('white captcha.png')

            curX, curY = win32gui.GetCursorPos()
            im.paste(captcha, box=(curX, curY), mask=captcha)

            fileName = "captchaTestWhite%d.jpg" % count
            print(fileName)
            im.save(fileName, "JPEG")
            toggle = False
        elif toggle is False:
            captcha = Image.open('dark captcha.png')

            curX, curY = win32gui.GetCursorPos()
            im.paste(captcha, box=(curX, curY), mask=captcha)

            fileName = "captchaTestDark%d.jpg" % count
            print(fileName)
            im.save(fileName, "JPEG")
            toggle = True
    if screenDecision == "3":
        im = ImageGrab.grab()
        chrome = Image.open('google-chrome-icon-small.png')

        curX, curY = win32gui.GetCursorPos()
        im.paste(chrome, box=(curX, curY), mask=chrome)

        fileName = "chrome%d.jpg" % count
        print(fileName)
        im.save(fileName, "JPEG")
        winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
    if screenDecision == "4":
        im = ImageGrab.grab()
        edge = Image.open('microsoft_edge_icon.png')

        curX, curY = win32gui.GetCursorPos()
        im.paste(edge, box=(curX, curY), mask=edge)

        fileName = "edge%d.jpg" % count
        print(fileName)
        im.save(fileName, "JPEG")
        winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
    if screenDecision == "5":
        im = ImageGrab.grab()

        fileName = "Desktop%d.jpg" % count
        print(fileName)
        im.save(fileName, "JPEG")
        winsound.PlaySound('sound.wav', winsound.SND_FILENAME)


    count = count + 1
    time.sleep(2)
winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
