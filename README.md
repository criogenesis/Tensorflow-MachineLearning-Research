# Multi-Object Detecotr
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
Once you've determined that your graphics card is compatible with CUDA, you need to install the newest Visual Studo using this link:
https://visualstudio.microsoft.com/downloads/

I installed Visual Studio 2019 using the community package
