import sys
# append facerec to module search path
sys.path.append("../..")
import cv2
from facedet.detector import SkinFaceDetector
import numpy as np
import os

# This is customized so that the picture also uses the clahe filter and store them in a different folder

def extract_faces(src_dir, dst_dir, clahe_dir, detector, face_sz = (130,130)):
	"""
	Extracts the faces from all images in a given src_dir and writes the extracted faces
	to dst_dir. Needs a facedet.Detector object to perform the actual detection.
	
	Args:
		src_dir [string] 
		dst_dir [string] 
		detector [facedet.Detector]
		face_sz [tuple] 
	"""

	clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

	if not os.path.exists(dst_dir):
		try:
			os.mkdir(dst_dir)
		except:
			raise OSError("Can't create destination directory (%s)!" % (dst_dir))
	for dirname, dirnames, filenames in os.walk(src_dir):
		for subdir in dirnames:
				src_subdir = os.path.join(dirname, subdir)
				dst_subdir = os.path.join(dst_dir,subdir)
				clahe_subdir = os.path.join(clahe_dir,subdir)
				if not os.path.exists(dst_subdir):
					try:
						os.mkdir(dst_subdir)
					except:
						raise OSError("Can't create destination directory (%s)!" % (dst_dir))
				if not os.path.exists(clahe_subdir):
					try:
						os.mkdir(clahe_subdir)
					except:
						raise OSError("Can't create destination directory (%s)!" % (dst_dir))
				for filename in os.listdir(src_subdir):
					name, ext = os.path.splitext(filename)
					src_fn = os.path.join(src_subdir,filename)
					img = cv2.imread(src_fn)
					rects = detector.detect(img)
					for i,rect in enumerate(rects):
						x0,y0,x1,y1 = rect
						face = img[y0:y1,x0:x1]
						gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
						claheIm = clahe.apply(gray)[y0:y1,x0:x1]
						cla = cv2.resize(claheIm, face_sz, interpolation = cv2.INTER_CUBIC)
						face = cv2.resize(face, face_sz, interpolation = cv2.INTER_CUBIC)
						print os.path.join(dst_subdir, "%s_%s_%d%s" % (subdir, name,i,ext))
						cv2.imwrite(os.path.join(dst_subdir, "%s_%s_%d%s" % (subdir, name,i,ext)), face)
						cv2.imwrite(os.path.join(clahe_subdir, "%s_%s_%d%s" % (subdir, name,i,ext)), cla)

if __name__ == "__main__":
	if len(sys.argv) < 3:
		print "usage: python extract_faces.py <src_dir> <dst_dir>"
		sys.exit()
	src_dir = sys.argv[1]
	dst_dir = sys.argv[2]
	clahe_dir = sys.argv[3]
	detector = SkinFaceDetector(threshold=0.3, cascade_fn="/home/kristin/AwesomeThings/QFace/haarcascade_frontalface_default.xml")
	extract_faces(src_dir=src_dir, dst_dir=dst_dir, clahe_dir=clahe_dir, detector=detector)
