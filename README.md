# qface
Detecting face of qers

Required:
* python 2.7
* scipy
* numpy
* opencv

# faceDetection

With the faceDetection you can create your own dataset. Specify the path where do you want to store the images.
Run the app with `python face_detection.py` 

# facerec

Download:
https://github.com/bytefish/facerec
A third party lib. facerec/py/apps/videofacerec opens a stream and detects faces that are trained in the *.pkl file.

Training a model:
`python simple_videofacerec.py -t /home/philipp/facerec/data/celebrities my_model.pkl`

This project is included as a submodule, please see the following link for instructions on cloning: http://git-scm.com/book/nl/v1/Git-tools-Submodules#Een-project-met-submodules-clonen

