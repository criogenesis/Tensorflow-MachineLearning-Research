'''
Created on May 4, 2019

@author: Zack
'''
#-- include('examples/showgrabfullscreen.py') --#
from PIL import ImageGrab
from PIL import Image
import time
import win32gui

NumberOfScreenshots = int(input("How many Screenshots would you like taken?:\n"))
count = 1

screenDecision = input("Will you be taking cursor screenshots or captcha? type 1 for cursor or 2 for captcha:\n")

toggle = True

while(count <= NumberOfScreenshots):
    if screenDecision == "1":
        im = ImageGrab.grab()
        cursor = Image.open('cursor.png')
        
        curX, curY = win32gui.GetCursorPos()
        im.paste(cursor,box=(curX,curY),mask=cursor)
        
        fileName = "cursorTest%d.jpg"%count
        print(fileName)
        im.save(fileName,"JPEG")
    if screenDecision == "2":
        im = ImageGrab.grab()
        if toggle is True:
            captcha = Image.open('white captcha.png')
        
            curX, curY = win32gui.GetCursorPos()
            im.paste(captcha,box=(curX,curY),mask=captcha)
            
            fileName = "captchaTestWhite%d.jpg"%count
            print(fileName)
            im.save(fileName,"JPEG")
            toggle = False
        elif toggle is False:
            captcha = Image.open('dark captcha.png')
        
            curX, curY = win32gui.GetCursorPos()
            im.paste(captcha,box=(curX,curY),mask=captcha)
            
            fileName = "captchaTestDark%d.jpg"%count
            print(fileName)
            im.save(fileName,"JPEG")
            toggle = True
   
    count = count + 1
    time.sleep(2)