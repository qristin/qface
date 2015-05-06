import sys
import cv2
import numpy as np
from PyQt4 import QtGui, QtCore, Qt
from ui import Ui_MainWindow
from utils import *


class Video():
    def __init__(self,capture, getFrame):
        self.capture = capture
        self.currentFrame=np.array([])
        self.getFrame = getFrame
        self.labels = []

    def captureNextFrame(self):
        frame, predictions = self.getFrame()
        if(len(predictions)>1):
            self.labels = get_text(predictions[0], predictions[-1])
        self.currentFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
        # capture frame and reverse RBG BGR and return opencv image
        # ret, readFrame=self.capture.read()
        # if(ret==True):
        #     self.currentFrame=cv2.cvtColor(readFrame,cv2.COLOR_BGR2RGB)

    def convertFrame(self):
        # converts frame to format suitable for QtGui 
        try:
            height,width=self.currentFrame.shape[:2]
            img=QtGui.QImage(self.currentFrame,
            width,
            height,
            QtGui.QImage.Format_RGB888)
            img=QtGui.QPixmap.fromImage(img)
            self.previousFrame = self.currentFrame
            return img
        except:
            return None

class Gui(QtGui.QMainWindow):
    def __init__(self,capture, getFrame, parent = None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.video = Video(capture, getFrame)
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self.play)
        self._timer.start(27)
        self.update()

    def play(self):
        try:
            self.video.captureNextFrame()
            self.ui.videoFrame.setPixmap(self.video.convertFrame())
            self.ui.videoFrame.setScaledContents(True)
            if(len(self.video.labels)!=0):
                self.ui.label1.setText(self.video.labels[0])
                self.ui.label2.setText(self.video.labels[1])
                self.ui.label3.setText(self.video.labels[2])
                self.ui.label4.setText(self.video.labels[3])
                self.ui.label5.setText(self.video.labels[4])
        except TypeError as e:
            print("No FRame", e)

def startGui(capture, getFrame):
    app = QtGui.QApplication(sys.argv)
    ex = Gui(capture, getFrame)
    ex.show()
    sys.exit(app.exec_())

# if __name__ == '__main__':
#     #cv2.
#     startgui()