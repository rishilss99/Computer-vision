import cv2
import numpy as np

image = cv2.imread("E:\Rishil's Documents\Python Programs 3\Computer Vision(Drishti Project)\Mastering OpenCV in Python(Udemy)\Master OpenCV\images\input.jpg")

h,w=image.shape[:2]
q_h,q_w=h/4,w/4

T = np.float32([[1,0,q_w],[0,1,q_h]]) #Numpy array of float32 type
rot_matrix = cv2.getRotationMatrix2D((w/2,h/2),90,1)
# translation = cv2.warpAffine(image,T,(w,h)) #3rd parameter is the dimensions of the window
cv2.imshow("Translation",cv2.transpose(image))
cv2.waitKey()
cv2.destroyAllWindows()