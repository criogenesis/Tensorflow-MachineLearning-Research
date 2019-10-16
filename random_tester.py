from PIL import ImageGrab
from PIL import Image
import time
import win32gui
import winsound
import random
from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()

time.sleep(2)

im = ImageGrab.grab()

width, height = im.size
firefox= Image.open('firefox_icon.png')

curX, curY = win32gui.GetCursorPos()

leftMin = curX - 284
leftMax = leftMin + 268
topMin = curY - 284
topMax = topMin + 268
print(curX, curY)
print(leftMin, topMin)
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
print(leftMin, topMin)
print(randomLeft, randomTop)
randomRight = randomLeft + 300
randomBottom = randomTop + 300

curX = curX - 16
curY = curY - 16
im.paste(firefox, box=(curX, curY), mask=firefox)
box = (randomLeft, randomTop, randomRight, randomBottom)
crop = im.crop(box)

fileName = "firefox%d.jpg" % 1
print(fileName)
crop.save(fileName, "JPEG")