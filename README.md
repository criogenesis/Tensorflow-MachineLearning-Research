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

once you extract the file, make sure you place it directly in the object detection folder located at 
```
(your path)/models/models-master/research/object_detection
```
*note that whenever I type (your path) in path directory I am expecting you to include whatever location you have decided to place the models folder in that contains everything.


I have decided to use the faster_rcnn_inception_v2_coco_2018_01_28 model, which is a very accurate model but can be taxing in terms of processing. For this reason a separate model can be used, but each model requires their own target loss to be achieved below. In this tutorial I will only be talking about the loss values for the faster_rcnn model.

# Image Labeling

In machine learning, the first thing you usually do when it comes to creating your own custom object detector is creating the custom dataset to train the model on. For each object you detect you're going to want around 100 to 200 images in your dataset that include that object. For the purposes of this project I created the screenshot.py program to help with generating the data I needed for all of the objects. This program takes a screenshot of the current screen and then where-ever the cursor is at the time of the screenshot, it masks a transparent png of the object in place of where the cursor currently is. This allows for faster data generation of raw desktop images that include the objects of interest. When trying to train the cursor and close box icon I decided to crop out a 300 x 300 box around the object randomly so that it would include the object that needed to be detected but was also variable up the data so that the object was not in the same location everytime. The main reason for cropping a 300 x 300 box around the small object is due to the aspect ratio difference between the desktop and the small cursor and close box icon. In my case a 1920 x 1080 desktop compared with a 30 x 30 sized cursor would be too great a size difference for Tensorflow to detect, 300 x 300 in comparison to 30 x 30 allowed much easier detection. The reCaptcha box was a separate case as it was noticebly bigger in comparison to the cursor and close box icon, so I cropped the reCaptcha images to be around 600 x 400 in size.

At this point, you need to make a folder named train and a folder named test. For each object that you are trying to detect you need to put 20% of the images in test and the rest of the images in train. As an example, if you have 100 images that contain Obect A and 100 images that contain Object B your test folder would contain 40 images (20 from Object A and 20 from Object B). The rest of the 60 images would be placed in the train folder. At this point, the train and test folders need to be placed in the images folder located in the object detection folder under:

```
(Your path)\models\models-master\research\object_detection\images
```


Once the dataset is generated, each object of interest in your dataset must be labeled with a bounding box so that Tensorflow knows what to train your detector on.

To do this, I used a program called LabelImg:
https://tzutalin.github.io/labelImg/

I reccommend downloading Windows 1.8.0 as this is the version I used in labeling my dataset.

When using LabelImg, you want to make sure that depending on the number of objects you're trying to detect, you make sure to label each object that is shown in your dataset with the name of the object in question. This is so that we can use the corresponding XML files that are generated for each image for training later on.

# Converting XML to CSV

At this point we're going to want to have the xml_to_csv.py file placed in the object detection folder so that we can run it in order to convert all of the XML files to CSV files for the next step. Once the script successfully runs, you should have train_labels and test_labels as csv files in the data folder in object detection.

# Creating TF_records

To create the TF_records we have to first modify and then run the generate_tfrecords.py script which also must be ran from inside the object detection folder.

The first edit will be starting at the def class_text_to_int(row_label) function at line 30:
```
def class_text_to_int(row_label):
    if row_label == 'captcha':
        return 1
    elif row_label == 'cursor':
        return 2
    elif row_label == 'close':
        return 3
    else:
        None
```

This is where you will be specifiying the name that you labeled your objects when using labelImg.

If you are only planning on detectiong one object the function will be changed to this:
```
def class_text_to_int(row_label):
    if row_label == '(your label here)':
        return 1
    else:
        None
```

Once you have edited the generate_tfrecord.py script you will need to run two separate commands in the cmd prompt while in the object detection folder. 

The first command will be for the train directory
```
python generate_tfrecord.py --csv_input=data\train_labels.csv --image_path=images\train --output_path=data\train.record
```
The second command will be for the test directory
```
python generate_tfrecord.py --csv_input=data\test_labels.csv --image_path=images\test --output_path=data\test.record
```

If you run across any errors with either commands, make sure that your data folder contains the train_labels.csv and test_labels.csv and that your images folder contains the test and train folder.

# Creating label maps

Once the tf records have been successfully created, you can create your label map, this file is necessary so that tensorflow knows what to label each object during detection.

You'll want to start by making an empty file of type .pbtxt and call it object-detection.pbtxt.
This is what my object-detection.pbtxt file looks like on the inside:
```
item {
  id: 1
  name: 'captcha'
}

item {
  id: 2
  name: 'cursor'
}

item {
  id: 3
  name: 'close'
}
```

If you notice, the id is the same exact number as the one associated with the function that we just changed in the generate_tfrecord.py script. For this reason, make sure the id's are associated with the correct object name to prevent confusion later on. (If you are only trying to detect one object, make sure you only have one item or it will mess with your training). 

Once the file is created, place it directly into the training folder inside of the object detection folder.
```
(your path)\models\models-master\research\object_detection\training
```

# Modifying model config file

To make things a little easier, i'm going to include my own config file in this repository. However, you will still need to make changes depending on your own file paths and number of objects being detected.

When you have the file, place it directly into the training folder just like we did with the pbtxt file.

the first change will be on line 9, this says num_classes and it's where you will type in the number of objects you're looking to detect.

the next change will be at line 107, and should be changed to look something like this
```
fine_tune_checkpoint: "(your path)/models/models-master/research/object_detection/faster_rcnn_inception_v2_coco_2018_01_28/model.ckpt"
```
*note that when copy and pasting file paths, it will most likely put back slashes in by default "\" you will need to change all of them to be foward slashes "/" as shown above so that the script can detect the correct file path

the next change will be starting at line 123, this will point the config file to your train.record file and your label map respectfully
```
train_input_reader: {
  tf_record_input_reader {
    input_path: "(your path)/models/models-master/research/object_detection/data/train.record"
  }
  label_map_path: "(your path)/models/models-master/research/object_detection/training/object-detection.pbtxt"
}
```

At line 129, you will need to change num examples to be the number of photos containted in your test directory. In my case I have 128 images so my num_examples is 128 respectively.

the last change will be at line line 137, it's fairly identical to what we changed in line 123.
In this case we are pointing to test.record instead of train.record, but it is the same label map:
```
eval_input_reader: {
  tf_record_input_reader {
    input_path: "(your path)/models/models-master/research/object_detection/data/test.record"
  }
  label_map_path: "(your path)/models/models-master/research/object_detection/training/object-detection.pbtxt"
  shuffle: false
  num_readers: 1
}
```

# Training process

At this point all files are ready and configured and you should be able to run the train.py script with (hopefully) no issues.

when in the object detection folder in cmd prompt you will want to enter this command:
```
python train.py --logtostderr --train_dir=training/ --pipeline_config_path=training/faster_rcnn_inception_v2_pets.config
```
*note that if you have previously trained a model using the above methods, make sure you delete everything except  your config file and your .pbtxt file or you will come across errors.

Ideally after a little bit of time everything will be recognized properly by tensorflow and you will start to train your model. At this point you will start to see a loss value being generated and changing in size (probably fairly drastically in the beginning). How fast your loss value drops will be entirely dependent on how powerful of a GPU you currently have. The faster the GPU the closer your loss value will be approaching your ideal loss value. For the faster_rcnn model that I am using you will want to be seeing a consistent loss value that is below 0.05. This could take some time, and to full understand where your loss is at overall you're going to want to open up tensorboard on another cmd prompt window.

# Using Tensorboard

Before you do run tensorboard, make sure that at least 10 minutes have gone by or that you have generated a new summary step in your training directory. These saved model steps are there in case you decide that you want to train the model later but need a place to leave off at a checkpoint. It is for this reason that it is highly reccommend you do not stop training until you have just generated a new summary step. When you do see that you have generated a summary step (that is not step 0) you can open up a cmd prompt window.


Once you have a new cmd prompt window open, make sure you are in your object detection folder and type the following command:
```
tensorboard --logdir=training
```

This will having tensorboard running at localhost, so while the you leave both the training cmd window and the tensorboard cmd window running in the background, you can open up an browser and type in the following:
http://localhost:6006
