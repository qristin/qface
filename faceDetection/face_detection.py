import cv2
import sys
from time import time
import os

PATH = "/home/kristin/AwesomeThings/QFace/img/captured"

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
glass_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

video_capture = cv2.VideoCapture(0)

coolDown = 10

face_sz = (130,130)

now = time()
storedTime = 0
f = []

for filename in os.listdir(PATH):
    name, ext = os.path.splitext(filename)
    try:
        intVal = int(name)
        f.append(intVal)
    except:
        value = "niks"
try:
    count = max(f)
except:
    count = 0

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        if 150<w and w<300:
            face = frame[y:y+h, x:x+w].copy()
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = glass_cascade.detectMultiScale(roi_gray)

            numberEyes = len(eyes)
            ey1 = 0
            eyeHeighDiff = 1000
            if numberEyes==2:
                for (ex,ey,ew,eh) in eyes:
                    if ey1 ==0:
                        ey1 = ey
                    else:
                        eyeHeighDiff = abs(ey1-ey)
                    cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,0,255),2)

            # glasses = glass_cascade.detectMultiScale(roi_gray)
            # for (ex,ey,ew,eh) in eyes:
            #     cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(255,0,255),2)

            if eyeHeighDiff<10:
                now = time()
                if (now-storedTime) > coolDown:
                    storedTime = now
                    equIm = cv2.equalizeHist(roi_gray)
                    cv2.imshow('img',equIm)
                    face = cv2.resize(face, face_sz, interpolation = cv2.INTER_CUBIC)
                    equ = cv2.resize(equIm, face_sz, interpolation = cv2.INTER_CUBIC)
                    cv2.imwrite(os.path.join(PATH, "%s%s%d%s" % ("","",count,".jpg")), equ)
                    count = count+1
                    print 'Save Image'
        

    # Display the resulting frame
    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()

# img = cv2.imread('img/face.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# faces = face_cascade.detectMultiScale(gray, 1.3, 5)
# # faces = face_cascade.detectMultiScale(
# #         gray,
# #         scaleFactor=1.1,
# #         minNeighbors=5,
# #         minSize=(30, 30),
# #         flags=cv2.cv.CV_HAAR_SCALE_IMAGE
# #     )
# for (x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#     print img
#     roi_gray = gray[y:y+h, x:x+w]
#     roi_color = img[y:y+h, x:x+w]
#     eyes = eye_cascade.detectMultiScale(roi_gray)
#     for (ex,ey,ew,eh) in eyes:
#         cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()