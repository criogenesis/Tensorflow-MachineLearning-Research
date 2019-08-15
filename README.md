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


