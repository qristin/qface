# qface
Detecting face of qers

Required:
* python 2.7
* scipy
* numpy
* opencv

# faceDetection

With the faceDetection you can create your own dataset. Specify the path where do you want to store the images.
Run the app with `python face_detection.py` on the path ./faceDetection/

# facerec

faceRecognition/apps/videofacerec opens a stream and detects faces that are trained in the *.pkl file.

Training a model:
On the path ./faceRecognition/apps/videofacerec/ run:
`python simple_videofacerec.py -t <path to your training images> my_model.pkl`

Run video with a trained pickle file:
`python simple_videofacerec.py my_model.pkl`

# extract faces
To make use of images from the internet we must extract faces

# TODO

* threshold  implementeren en visualiseren

# DONE

* weighted k nearest neighbour implementeren