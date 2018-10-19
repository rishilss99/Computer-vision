import cv2
import numpy as np

image = cv2.imread(r"E:\Rishil's Documents\Python Programs 3\Computer Vision(Drishti Project)\Mastering OpenCV in Python(Udemy)\Master OpenCV\images\house.jpg")

original_image = image.copy()
gray = cv2.cvtColor(original_image,cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(gray,30,200)

_,contours,heirarchy = cv2.findContours(edged.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
for c in contours:
    x,y,w,h = cv2.boundingRect(c)
    cv2.rectangle(original_image,(x,y),(x+w,y+h),(0,255,0),2)
    cv2.imshow("Orignial image",original_image)

for c in contours:
    accuracy = 0.05 * cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,accuracy,True)
    cv2.drawContours(image,[approx],0,(0,0,255),2)
    cv2.imshow("Approx",image)

cv2.imshow("Image",original_image)
cv2.waitKey()
cv2.destroyAllWindows()
