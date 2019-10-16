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
import random
from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()


NumberOfScreenshots = int(input("How many Screenshots would " +
                                "you like taken?:\n"))

count = 1
screenDecision = input(
    "Type 1 for cursor\n2 for captcha\n3 for chrome icon\n" +
    "4 for edge icon\n5 for firefox icon\n" +
    "or 6 for opera icon: \n")

DeskOrMask = input("type 1 for masked screenshot or 2 for desktop screenshot:\n")

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
        if DeskOrMask == "1":
            im = ImageGrab.grab()
            chrome = Image.open('google-chrome-icon-small.png')

            curX, curY = win32gui.GetCursorPos()
            im.paste(chrome, box=(curX, curY), mask=chrome)

            fileName = "chrome%d.jpg" % count
            print(fileName)
            im.save(fileName, "JPEG")
            winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
        else:
            im = ImageGrab.grab()

            fileName = "chrome%d.jpg" % (count+100)
            print(fileName)
            im.save(fileName, "JPEG")
            winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
    if screenDecision == "4":
        if DeskOrMask == "1":
            im = ImageGrab.grab()
            width, height = im.size
            edge = Image.open('microsoft_edge_icon.png')

            curX, curY = win32gui.GetCursorPos()

            leftMin = curX - 286
            leftMax = leftMin + 272
            topMin = curY - 286
            topMax = topMin + 272

            if (topMax + 300) > height:
                topMax = height - 300
            if (topMin - 286) < 0:
                topMin = 0
            if (leftMax + 300) > width:
                leftMax = width - 300
            if (leftMin - 286) < 0:
                leftMin = 0

            randomLeft = random.randint(leftMin-1, leftMax)
            randomTop = random.randint(topMin-1, topMax)
            randomRight = randomLeft + 300
            randomBottom = randomTop + 300

            curX = curX - 14
            curY = curY - 14
            im.paste(edge, box=(curX, curY), mask=edge)
            box = (randomLeft, randomTop, randomRight, randomBottom)
            crop = im.crop(box)

            fileName = "edge%d.jpg" % count
            print(fileName)
            crop.save(fileName, "JPEG")
            winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
        else:
            im = ImageGrab.grab()

            width, height = im.size
            curX, curY = win32gui.GetCursorPos()

            curX = curX - 38

            leftMin = curX - 276
            leftMax = leftMin + 252
            topMin = curY - 276
            topMax = topMin + 252

            if (topMax + 300) > height:
                topMax = height - 300
            if (topMin) < 0:
                topMin = 0
            if (leftMax + 300) > width:
                leftMax = width - 300
            if (leftMin) < 0:
                leftMin = 0

            randomLeft = random.randint(leftMin-1, leftMax)
            randomTop = random.randint(topMin-1, topMax)
            randomRight = randomLeft + 300
            randomBottom = randomTop + 300

            curX = curX - 24
            curY = curY - 24
            box = (randomLeft, randomTop, randomRight, randomBottom)
            crop = im.crop(box)

            fileName = "edge%d.jpg" % (count+100)
            print(fileName)
            crop.save(fileName, "JPEG")
            winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
    if screenDecision == "5":
        if DeskOrMask == "1":
            im = ImageGrab.grab()

            width, height = im.size
            firefox= Image.open('firefox_icon.png')

            curX, curY = win32gui.GetCursorPos()

            leftMin = curX - 284
            leftMax = leftMin + 268
            topMin = curY - 284
            topMax = topMin + 268

            if (topMax + 300) > height:
                topMax = height - 300
            if (topMin) < 0:
                topMin = 0
            if (leftMax + 300) > width:
                leftMax = width - 300
            if (leftMin) < 0:
                leftMin = 0

            randomLeft = random.randint(leftMin-1, leftMax)
            randomTop = random.randint(topMin-1, topMax)
            randomRight = randomLeft + 300
            randomBottom = randomTop + 300

            curX = curX - 16
            curY = curY - 16
            im.paste(firefox, box=(curX, curY), mask=firefox)
            box = (randomLeft, randomTop, randomRight, randomBottom)
            crop = im.crop(box)

            fileName = "firefox%d.jpg" % count
            print(fileName)
            crop.save(fileName, "JPEG")
            winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
        else:
            im = ImageGrab.grab()
            width, height = im.size
            curX, curY = win32gui.GetCursorPos()

            curX = curX - 38

            leftMin = curX - 276
            leftMax = leftMin + 252
            topMin = curY - 276
            topMax = topMin + 252

            if (topMax + 300) > height:
                topMax = height - 300
            if (topMin) < 0:
                topMin = 0
            if (leftMax + 300) > width:
                leftMax = width - 300
            if (leftMin) < 0:
                leftMin = 0

            randomLeft = random.randint(leftMin-1, leftMax)
            randomTop = random.randint(topMin-1, topMax)
            randomRight = randomLeft + 300
            randomBottom = randomTop + 300

            curX = curX - 24
            curY = curY - 24
            box = (randomLeft, randomTop, randomRight, randomBottom)
            crop = im.crop(box)

            fileName = "firefox%d.jpg" % (count+100)
            print(fileName)
            crop.save(fileName, "JPEG")
            winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
    if screenDecision == "6":
        if DeskOrMask == "1":
            im = ImageGrab.grab()
            width, height = im.size
            opera= Image.open('opera_icon.png')

            curX, curY = win32gui.GetCursorPos()

            leftMin = curX - 284
            leftMax = leftMin + 268
            topMin = curY - 284
            topMax = topMin + 268

            if (topMax + 300) > height:
                topMax = height - 300
            if (topMin - 284) < 0:
                topMin = 0
            if (leftMax + 300) > width:
                leftMax = width - 300
            if (leftMin - 284) < 0:
                leftMin = 0

            randomLeft = random.randint(leftMin-1, leftMax)
            randomTop = random.randint(topMin-1, topMax)
            randomRight = randomLeft + 300
            randomBottom = randomTop + 300

            curX = curX - 16
            curY = curY - 16
            im.paste(firefox, box=(curX, curY), mask=firefox)
            box = (randomLeft, randomTop, randomRight, randomBottom)
            crop = im.crop(box)

            fileName = "opera%d.jpg" % count
            print(fileName)
            crop.save(fileName, "JPEG")
            winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
        else:
            im = ImageGrab.grab()

            width, height = im.size
            curX, curY = win32gui.GetCursorPos()

            curX = curX - 38

            leftMin = curX - 276
            leftMax = leftMin + 252
            topMin = curY - 276
            topMax = topMin + 252

            if (topMax + 300) > height:
                topMax = height - 300
            if (topMin) < 0:
                topMin = 0
            if (leftMax + 300) > width:
                leftMax = width - 300
            if (leftMin) < 0:
                leftMin = 0

            randomLeft = random.randint(leftMin-1, leftMax)
            randomTop = random.randint(topMin-1, topMax)
            randomRight = randomLeft + 300
            randomBottom = randomTop + 300

            curX = curX - 24
            curY = curY - 24
            box = (randomLeft, randomTop, randomRight, randomBottom)
            crop = im.crop(box)

            fileName = "opera%d.jpg" % (count+100)
            print(fileName)
            crop.save(fileName, "JPEG")
            winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
        winsound.PlaySound('sound.wav', winsound.SND_FILENAME)



    count = count + 1
    #time.sleep(2)
winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
winsound.PlaySound('sound.wav', winsound.SND_FILENAME)
