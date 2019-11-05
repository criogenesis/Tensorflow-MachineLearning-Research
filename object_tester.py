

import Multi_Object_Detect_Function as mod
import pyautogui as pyag
import time

testlist = ['chrome', 'firefox', 'edge', 'opera']

result_dict = mod.recieve_object(testlist)
print(result_dict)
for key, value in result_dict.items():
    left = value[0]
    right = value[1]
    top = value[2]
    bottom = value[3]
    print(key, value)
    if key == "chrome":
        average_width = (left + right)/2
        average_height = (top + bottom)/2
        break
    elif key == "firefox":
        average_width = (left + right)/2
        average_height = (top + bottom)/2
        break
    elif key == "edge":
        average_width = (left + right)/2
        average_height = (top + bottom)/2
        break
    elif key == "opera":
        average_width = (left + right)/2
        average_height = (top + bottom)/2
        break
time.sleep(2)
pyag.moveTo(average_width, average_height, duration=1)
