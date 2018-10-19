import cv2
import os
import numpy as np

image = cv2.imread("E:\Pictures\Saved Pictures\College Photos\DSC_0145.jpg",0)
new = cv2.resize(image,(800,600),interpolation=cv2.INTER_LANCZOS4)
harr_classifier = cv2.CascadeClassifier("E:\Rishil's Documents\Python Programs 3\Computer Vision(Drishti Project)\Mastering OpenCV in Python(Udemy)\Master OpenCV\Haarcascades\haarcascade_frontalface_default.xml")
faces = harr_classifier.detectMultiScale(new,scaleFactor=1.1,minNeighbors=5)
for x,y,w,h in faces:
    cv2.rectangle(new,(x,y),(x+w,y+h),(0,255,0),4)
print(len(faces))
cv2.imshow("Image",new)
cv2.waitKey()
cv2.destroyAllWindows()