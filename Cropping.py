import cv2
import numpy as np

image = cv2.imread("E:\Rishil's Documents\Python Programs 3\Computer Vision(Drishti Project)\Mastering OpenCV in Python(Udemy)\Master OpenCV\images\input.jpg")

height,width=image.shape[:2]
start_row,start_col=int(0.25*height),int(0.25*width)
end_row,end_col=int(0.75*height),int(0.75*width)

cropped = image[start_row:end_row,start_col:end_col]
cv2.imshow("Cropped",cropped)
cv2.waitKey()
cv2.destroyAllWindows()

