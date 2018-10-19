import cv2
import numpy as np
image = cv2.imread(r"E:\Rishil's Documents\Python Programs 3\Computer Vision(Drishti Project)\Mastering OpenCV in Python(Udemy)\Master OpenCV\images\input.jpg")
cv2.imshow("Yolo",image)
cv2.waitKey()
cv2.destroyAllWindows()
print(image.shape)
