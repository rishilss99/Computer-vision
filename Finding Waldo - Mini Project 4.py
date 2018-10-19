import cv2
import numpy as np

image = cv2.imread(r"E:\Rishil's Documents\Python Programs 3\Computer Vision(Drishti Project)\Mastering OpenCV in Python(Udemy)\Master OpenCV\images\WaldoBeach.jpg")

cv2.imshow("Waldo beach",image)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.waitKey()
template = cv2.imread(r"E:\Rishil's Documents\Python Programs 3\Computer Vision(Drishti Project)\Mastering OpenCV in Python(Udemy)\Master OpenCV\images\Waldo.jpg",0)

result = cv2.matchTemplate(gray,template,cv2.TM_CCOEFF)
min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)

top_left = max_loc
bottom_right = (top_left[0] + 50, top_left[1] + 50)
cv2.rectangle(image, top_left, bottom_right, (0,0,255), 5)

cv2.imshow('Where is Waldo?', image)
cv2.waitKey()

cv2.destroyAllWindows()
