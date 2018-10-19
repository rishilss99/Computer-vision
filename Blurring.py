import cv2
import numpy as np

image = cv2.imread("E:\Rishil's Documents\Python Programs 3\Computer Vision(Drishti Project)\Mastering OpenCV in Python(Udemy)\Master OpenCV\images\elephant.jpg")

kernel_5x5=np.ones((5,5),np.float32)/25
blurred = cv2.filter2D(image,-1,kernel_5x5)
cv2.imshow("Blurred",blurred)
cv2.waitKey()
cv2.destroyAllWindows()