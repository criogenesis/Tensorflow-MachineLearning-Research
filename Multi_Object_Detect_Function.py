# Image Object Detection Using Tensorflow-trained Classifier #
#
# Author: Zack Tuttle
# Date: 7/8/19
# Description:
# This program uses Tensorflow Object Detection to detect a cursor in a given
# desktop image.

# Some of the code is copied from Google's example at
# https://github.com/tensorflow/models/blob/master/research/object_detection/object_detection_tutorial.ipynb

# and some is copied from Dat Tran's example at
# https://github.com/datitran/object_detector_app/blob/master/object_detection_app.py

# the meat of the code was provided by youtuber EdjeElectronics
# https://github.com/EdjeElectronics/TensorFlow-Object-Detection-API-Tutorial-Train-Multiple-Objects-Windows-10/blob/master/Object_detection_image.py

# partial crop code modified using this stackoverflow post
# https://stackoverflow.com/questions/5953373/how-to-split-image-into-multiple-pieces-in-python


# Import packages
from utils import visualization_utils as vis_util
from utils import label_map_util
import os
import cv2
import numpy as np
import tensorflow as tf
from PIL import Image
from PIL import ImageGrab

import win32gui
from ctypes import windll
user32 = windll.user32
user32.SetProcessDPIAware()

# Name of the directory containing the object detection module we're using
MODEL_NAME = 'inference_graph'

# Grab path to current working directory
CWD_PATH = os.getcwd()

# Path to frozen detection graph .pb file, which contains the model that is
# used
# for object detection.
PATH_TO_CKPT = os.path.join(CWD_PATH, MODEL_NAME, 'frozen_inference_graph.pb')

# Path to label map file
PATH_TO_LABELS = os.path.join(CWD_PATH, 'training', 'object-detection.pbtxt')

# Number of classes the object detector can identify
# If you are trying to detect more objects than this number
# your label may appear as "N/A" instead of the name of your object.
NUM_CLASSES = 4

# Load the label map.
# Label maps map indices to category names, so that when the convolution
# network predicts `1`, we know that this corresponds to a `cursor`.
# Here we use internal utility functions, but anything that returns a
# dictionary mapping integers to appropriate string labels would be fine
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(
    label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)

# Load the Tensorflow model into memory.
detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

    sess = tf.Session(graph=detection_graph)

# Define input and output tensors (i.e. data) for the object detection
# classifier

# Input tensor is the image
image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

# Output tensors are the detection boxes, scores, and classes
# Each box represents a part of the image where a particular object was
# detected
detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

# Each score represents level of confidence for each of the objects.
# The score is shown on the result image, together with the class label.
detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

# Number of objects detected
num_detections = detection_graph.get_tensor_by_name('num_detections:0')

####################################################################


def recieve_object(object_to_detect_list):

    is_cursor_included = False
    is_chrome_included = False
    is_firefox_included = False
    is_edge_included = False
    is_opera_included = False

    object_and_coords_dict = {}

    for x in object_to_detect_list:
        if(x == 'cursor'):
            is_cursor_included = True
        elif(x == 'chrome'):
            is_chrome_included = True
        elif(x == 'firefox'):
            is_firefox_included = True
        elif(x == 'edge'):
            is_edge_included = True
        elif(x == 'opera'):
            is_opera_included = True

    # variables to be used for splicing
    # 300 is chosen as the default as the cursor and close box objects were trained
    # using images of that size.
    chopsizeWidth = 300
    chopsizeHeight = 300

    # img is a 1920 x 1080(or whatever is the resolution of your current monitor)
    # desktop picture that is saved
    # as in Image Object

    img = ImageGrab.grab()

    # width and height to be used as limits while iterating through cropped squares
    # As an example, width would equal 1920 and height would equal 1080
    width, height = img.size

    # initial overlaps for the beginning crops of any image.
    overlapx = 0
    overlapy = 0

    # count variables are initialized here
    count = 0
    countIntro = 0

    # overlap is declared for later use
    # This is done in order to account for overlap when cropping so that a crop
    # does not miss
    # and pass over a potential object that is detectable by the model and is
    # subject to change.
    overlapWidth = 40
    overlapHeight = 40

    # initializing percent, so that it can be used as a minimum to see the highest
    # possible bounding box detection percent
    cursor_percent_num = 0
    captcha_percent_num = 0
    chrome_percent_num = 0
    firefox_percent_num = 0
    edge_percent_num = 0
    opera_percent_num = 0

    # opera
    operaCoords = ()

    # edge
    edgeCoords = ()

    # firefox
    firefoxCoords = ()

    # cursor
    cursorImage = None
    cursorCoords = ()

    # captcha
    captchaImage = None
    captchaCoords = ()

    # chrome
    chromeImage = None
    chromeCoords = ()

    # close
    closeCoordList = []
    closeImageList = []

    # x0 coordinates stay constant while the inner for loop changes the y0 values
    # each of the for loops start at 0 and iterate by the chopsize up until either
    # the width(first for loop), or the height(second for loop).
    for x0 in range(0, width+chopsizeWidth, chopsizeWidth):
        # The purpose of this if statement, is for the cropped squares in the
        # first column after the first square
        # This is because in the very first cropped square,
        # there exists no overlap.
        # every square after will have an overlapx of 30
        if(count > 0):
            overlapx = overlapx + overlapHeight
        for y0 in range(0, height, chopsizeHeight):

            # This if statement makes sure that every cropped square after
            # the first column has an overlapy of 40, allowing overlap between
            # columns 1 and 2, and then 2 and 3 and so on.
            if(countIntro == 1):
                overlapy = overlapy + overlapWidth
            # print((y0, x0))
            # box = (x0-overlapx, y0-overlapy,
            #        x0+chopsizeWidth-overlapx,
            #        y0+chopsizeHeight-overlapy)

            box = ((width-chopsizeWidth if x0+chopsizeWidth-overlapx > width
                    else x0-overlapx),
                   (height-chopsizeHeight if y0+chopsizeHeight-overlapy > height
                    else y0-overlapy),
                   (width if x0+chopsizeWidth-overlapx > width
                    else x0+chopsizeWidth-overlapx),
                   (height if y0+chopsizeHeight-overlapy > height
                    else y0+chopsizeHeight-overlapy))

            image = np.array(img.crop(box))
            image_expanded = np.expand_dims(image, axis=0)

            # Perform the actual detection
            # by running the model with the image as input
            (boxes, scores, classes, num) = sess.run(
                [detection_boxes, detection_scores,
                 detection_classes, num_detections],
                feed_dict={image_tensor: image_expanded})
            # Draw the results of the detection (aka 'visulaize the results')
            (image, box_dict) = vis_util.visualize_boxes_and_labels_on_image_array(
                image,
                np.squeeze(boxes),
                np.squeeze(classes).astype(np.int32),
                np.squeeze(scores),
                category_index,
                use_normalized_coordinates=True,
                line_thickness=2,
                min_score_thresh=0.60)

            close_bool = False

            for key, value in box_dict.items():
                box_left = int(box[0] + value[0])
                box_right = int(box[0] + value[1])
                box_bottom = int(box[1] + value[2])
                box_top = int(box[1] + value[3])
                print((box_left, box_right, box_bottom, box_top))
                if key != 'test':
                    elements = key.split()
                    name = elements[0].strip(":")
                    percent = elements[1].split('%')[0]
                    percent_temp = int(percent)
                    if name == "cursor" and percent_temp > cursor_percent_num and is_cursor_included:
                        cursor_percent_num = percent_temp
                        cursorImage = image
                        cursorCoords = (box_left, box_right, box_bottom, box_top)
                        object_and_coords_dict.update({name: cursorCoords})
                    if name == "captcha" and percent_temp > captcha_percent_num:
                        captcha_percent_num = percent_temp
                        captchaImage = image
                        captchaCoords = value
                    if (name == "chrome" and percent_temp >
                            chrome_percent_num and is_chrome_included):
                        chrome_percent_num = percent_temp
                        chromeCoords = (box_left, box_right, box_bottom, box_top)
                        object_and_coords_dict.update({name: chromeCoords})
                    if (name == "firefox" and percent_temp >
                            firefox_percent_num and is_firefox_included):
                        firefox_percent_num = percent_temp
                        firefoxCoords = (box_left, box_right, box_bottom, box_top)
                        object_and_coords_dict.update({name: firefoxCoords})
                    if (name == "edge" and percent_temp >
                            edge_percent_num and is_edge_included):
                        edge_percent_num = percent_temp
                        edgeCoords = (box_left, box_right, box_bottom, box_top)
                        object_and_coords_dict.update({name: edgeCoords})
                    if (name == "opera" and percent_temp >
                            opera_percent_num and is_opera_included):
                        opera_percent_num = percent_temp
                        operaCoords = (box_left, box_right, box_bottom, box_top)
                        object_and_coords_dict.update({name: operaCoords})
                    if name == "close":
                        closeCoords = value
                        closeCoordList.append(closeCoords)
                        if close_bool is False:
                            closeImageList.append(image)
                            close_bool = True

            countIntro = countIntro + 1
            # print(key, value)
            # print("tag is " + name)
            # print('%s %s' % (infile, box))
            # print(box)
        count = count + 1
        countIntro = 0
        overlapy = 0

    return object_and_coords_dict
