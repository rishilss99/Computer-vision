import cv2
import numpy as np

image = cv2.imread("E:\Rishil's Documents\Python Programs 3\Computer Vision(Drishti Project)\Mastering OpenCV in Python(Udemy)\Master OpenCV\images\shapes.jpg")

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray,30,200)

_,contours,heirarchy = cv2.findContours(edged.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)

print(cv2.moments(contours[0]))

cv2.drawContours(image,contours,-1,(0,255,0),3)
for i in contours:
    print(cv2.contourArea(i))
cv2.imshow("Image",image)
cv2.waitKey()
cv2.destroyAllWindows()