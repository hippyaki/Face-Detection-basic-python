import cv2
import os

cascPath=os.path.dirname(cv2.__file__)+"data.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frames = video_capture.read()

    gray = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)

    cv2 = imread.('data.xml')
     change = cv2.split(',')
