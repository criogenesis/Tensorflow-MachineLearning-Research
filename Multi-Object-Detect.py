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
import os
import cv2
import numpy as np
import tensorflow as tf
from PIL import Image

# Import utilites
from utils import label_map_util
from utils import visualization_utils as vis_util


# Name of the image being processed
infile = 'cursortest21.jpg'

# variables to be used for splicing
# 300 is chosen as the default as the cursor and close box objects were trained
# using images of that size.
chopsizeWidth = 300
chopsizeHeight = 300


isFirstColumn = True

# img is a 1920 x 1080(or whatever is the resolution of your current monitor)
# desktop picture that is saved
# as in Image Object
img = Image.open(infile)

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
percentNum = 0

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
NUM_CLASSES = 3

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

# x0 coordinates stay constant while the inner for loop changes the y0 values
# each of the for loops start at 0 and iterate by the chopsize up until either
# the width(first for loop), or the height(second for loop).
for x0 in range(0, width, chopsizeWidth):
    for y0 in range(0, height, chopsizeHeight):

        # The purpose of this if statement, is for the cropped squares in the
        # first column after the first square
        # This is because in the very first cropped square,
        # there exists no overlap.
        # every square after will have an overlapx of 30
        if(count == 1 and isFirstColumn):
            overlapx = overlapx + overlapHeight
            isFirstColumn = False
        print(overlapy)
        # This if statement makes sure that every cropped square after
        # the first column has an overlapy of 40, allowing overlap between
        # columns 1 and 2, and then 2 and 3 and so on.
        if(countIntro == 1):
            overlapy = overlapy + overlapWidth

        box = (x0-overlapx, y0-overlapy,
               x0+chopsizeWidth-overlapx,
               y0+chopsizeHeight-overlapy)

        image = np.array(img.crop(box))
        image_expanded = np.expand_dims(image, axis=0)

        # Perform the actual detection
        # by running the model with the image as input
        (boxes, scores, classes, num) = sess.run(
            [detection_boxes, detection_scores,
             detection_classes, num_detections],
            feed_dict={image_tensor: image_expanded})
        # Draw the results of the detection (aka 'visulaize the results')
        (image, xmin, percentMessage) = vis_util.visualize_boxes_and_labels_on_image_array(
            image,
            np.squeeze(boxes),
            np.squeeze(classes).astype(np.int32),
            np.squeeze(scores),
            category_index,
            use_normalized_coordinates=True,
            line_thickness=4,
            min_score_thresh=0.60)
        cv2.imshow('detector', image)
        cv2.waitKey(0)
        if percentMessage != 'test':
            elements = percentMessage[0].split()
            percent = elements[1].split('%')[0]
            percentTemp = int(percent)
            if percentTemp > percentNum:
                percentNum = percentTemp
                finalImage = image
                print(percentNum)

        countIntro = countIntro + 1
        print('%s %s' % (infile, box))
    count = count + 1
    countIntro = 0
    overlapy = 0
###############################################################################


# Press any key to close the image
cv2.imshow('Object detector', finalImage)
cv2.waitKey(0)

# Clean up
cv2.destroyAllWindows()
