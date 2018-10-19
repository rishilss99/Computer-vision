import cv2
import numpy as np

image = cv2.imread("E:\Rishil's Documents\Python Programs 3\Computer Vision(Drishti Project)\Mastering OpenCV in Python(Udemy)\Master OpenCV\images\input.jpg")

inter = cv2.resize(image,None,fx=2,fy=2,interpolation=cv2.INTER_LANCZOS4)
pyramid = cv2.pyrUp(image)

cv2.imshow("Inter",inter)
cv2.imshow("Pyramid",pyramid)
cv2.waitKey()
cv2.destroyAllWindows()