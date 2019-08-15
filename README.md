# Multi-Object Detector
The purpose of this project was to create software using tensorflows object detection api to be able to detect a cursor, reCaptcha box, as well as the close button at the top right of a window. It includes the trained models as well as all the data used for training the models.
Some modifications were made in the tensorflow sourcecode in order to get the python script to run and will be mentioned below.

# Installing Tensorflow-GPU

The majority of this tutorial will be referencing a youtube tutorial on installing tensorflow gpu for windows 10:
https://www.youtube.com/watch?v=KZFn0dvPZUQ

I would like to first mention that it is entirely possible to run Tensorflow primarily using a CPU. However, the processing speed will be greatly reduced compared to usilizing a GPU, so I will only be talking about the Tensorflow-GPU installation.

That being said, Tensorflow-GPU requires a CUDA compatible graphics card in order to run, this means if you do not have a compatible graphics card you will not be able to run Tensorflow otherwise.

# GPU compatiability with CUDA

If you do not have a Nvidia GPU or you are unsure if your graphics card is compatible this site will tell you if your graphics card is compatible or not:
https://developer.nvidia.com/cuda-gpus


# Visual Studio

Once you've determined that your graphics card is compatible with CUDA, you need to install the newest Visual Studio using this link:
https://visualstudio.microsoft.com/downloads/

I installed Visual Studio 2019 using the community package

# Installing CUDA

Before installing CUDA, we have to make sure we're using the most up to date version with Tensorflow using this link:
https://www.tensorflow.org/install/gpu

At the time of this tutorial, CUDA version 10.0 is the reccommended version to install:
https://developer.nvidia.com/cuda-10.0-download-archive

# Installing cuDNN

Once the correct version of CUDA is installed we have to install cuDNN using this link:
https://developer.nvidia.com/rdp/cudnn-download

The site will initially ask you for to login, this means you will have to make a nVidia account if you do not already have one.
Once the account is made, you can login and access the downloads section.

Select (Download cuDNN v7.6.2 (July 22, 2019), for CUDA 10.0)
as well as (cuDNN Library for Windows 10) under the drop down menu.

Once you have the package downloaded, you're going to need to unzip the rar file and be ready to copy the contents over to your current CUDA directory

For me, CUDA was found at C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0

Oncce you're in the v10.0 folder, you're going to want to copy the bin,include, and lib folder from your cuda folder (extracted from the zip) into the v10.0 folder and overwrite the files present.

# Setting up Environment Variables

The next step is to settup the necessary paths in environment variables so Tensorflow knows where to look for all the CUDA dependencies.

In the windows search bar you can type envi and a prompt to "Edit the system environment variables" should show up, click that.

In System Properties, go down to the bottom and click Environment Variables.

Under User Variables, you're going to want to click Path and edit it, we're going to be adding two new paths for the purpose of this tutorial.
```
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\bin
C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.0\libnvvp
```
You will also need to add a new path called PYTHONPATH and I reccommend adding the following paths:
```
C:\Users\hakku\Downloads\models\models-master\research\object_detection\utils
C:\Users\hakku\Downloads\models\models-master\research\object_detection
C:\Users\hakku\Downloads\models\models-master\research
C:\Users\hakku\Downloads\models\models-master\research\slim
C:\Users\hakku\Downloads\models\models-master
C:\Users\hakku\Downloads\models\models-master\research\object_detection\training
```
This path is entirely dependent on where you decide to keep your models folder which will be discussed in the model training section.
Make sure you are using the correct path for your settup.

When you've added these paths, click Ok on all corresponding windows



# Prerequesites and Dependencies

At this point it is assumed you already have Python installed and will not be covered in this tutorial.
To keep up with consistency I reccommend you install version 3.7 as this is the version I will be using.
I also highly reccommending that if you do not already to have the to your current python version added to the Path section in Environment Variables like we previously did with CUDA. 

C:\Users\hakku\AppData\Local\Programs\Python\Python37\
C:\Users\hakku\AppData\Local\Programs\Python\Python37\Scripts\
(example of my python directories in Path)

This allows you to be able to run any python script in the cmd window in any directory.

going forward now, all prerequistes will be installed using pip, so it is highly reccommended to have the newest version of pip to be able to run these cmds in your cmd prompt window.

All below pip installs are required both to run Tensorflow as well as run the scripts in this project
```
pip install --ignore-installed --upgrade tensorflow-gpu
pip install keras
pip install pandas
pip install numpy
pip install pillow
pip install lxml
pip install Cython
pip install contextlib2
pip install jupyter
pip install matplotlib
pip install opencv-python
pip install win32gui
```
# Training your own object model

This section serves two purposes, it serves to first show others how they can train their own object detectors if they desire to add-on to my current detected objects or to to detect objects of their own. It also serves as a sort of tutorial on showing how exactly I developed and trained my own model for my three detected objects.

For the purposes of this section, I will be referencing this youtube video:
https://www.youtube.com/watch?v=Rgpfk6eYxJA&t=1s

First you need to make sure you download the Tensorflow model folder at https://github.com/tensorflow/models
When you decide to extract the rar file, make sure that you remove the second models folder that is contained in the first after extracting the rar file. To do this, you will have to go into the second models folder, copy the models-master folder, paste it in the first models folder, and delete the now empty second models folder 

This will alter your path from
```
models/models/models-master
````
to
```
models/models-master
```

Just make sure you do not delete the models-master folder as that contains all of the important files for this project.

Next, we're going to need to use a model to use as a basis for training so we can use transfer learning:
http://download.tensorflow.org/models/object_detection/faster_rcnn_inception_v2_coco_2018_01_28.tar.gz

I have decided to use the faster_rcnn_inception_v2_coco_2018_01_28 model, which is a very accurate model but can be taxing in terms of processing. For this reason a separate model can be used, but each model requires their own target loss to be achieved below. In this tutorial I will only be talking about the loss values for the faster_rcnn model.

# Image Labeling

In machine learning, the first thing you usually do when it comes to creating your own custom object detector is creating the custom dataset to train the model on. For each object you detect you're going to want around 100 to 200 images in your dataset that include that object. For the purposes of this project I created the screenshot.py program to help with generating the data I needed for all of the objects. This program takes a screenshot of the current screen and then where-ever the cursor is at the time of the screenshot, it masks a transparent png of the object in place of where the cursor currently is. This allows for faster data generation of raw desktop images that include the objects of interest. When trying to train the cursor and close box icon I decided to crop out a 300 x 300 box around the object randomly so that it would include the object that needed to be detected but was also variable up the data so that the object was not in the same location everytime. The main reason for cropping a 300 x 300 box around the small object is due to the aspect ratio difference between the desktop and the small cursor and close box icon. In my case a 1920 x 1080 desktop compared with a 30 x 30 sized cursor would be too great a size difference for Tensorflow to detect, 300 x 300 in comparison to 30 x 30 allowed much easier detection. The reCaptcha box was a separate case as it was noticebly bigger in comparison to the cursor and close box icon, so I cropped the reCaptcha images to be around 600 x 400 in size.

At this point, you need to make a folder named train and a folder named test. For each object that you are trying to detect you need to put 20% of the images in test and the rest of the images in train. As an example, if you have 100 images that contain Obect A and 100 images that contain Object B

Once the dataset is generated, each object of interest in your dataset must be labeled with a bounding box so that Tensorflow knows what to train your detector on.

To do this, I used a program called LabelImg:
https://tzutalin.github.io/labelImg/

I reccommend downloading Windows 1.8.0 as this is the version I used in labeling my dataset.

When using LabelImg, you want to make sure that depending on the number of objects you're trying to detect, you make sure to label each object that is shown in your dataset with the name of the object in question. This is so that we can use the corresponding XML files that are generated for each image for training later on.
