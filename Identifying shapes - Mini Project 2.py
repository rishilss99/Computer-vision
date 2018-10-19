import cv2
import numpy as np

image = cv2.imread(r"E:\Rishil's Documents\Python Programs 3\Computer Vision(Drishti Project)\Mastering OpenCV in Python(Udemy)\Master OpenCV\images\someshapes.jpg")
dup = image.copy()
cv2.imshow("Image",image)
cv2.waitKey()

gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 127, 255, 1)

_,contours,heirarchy = cv2.findContours(thresh.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)

# cv2.drawContours(dup,contours,-1,(0,255,0),3)
# cv2.imshow("Contours",dup)
# cv2.waitKey()

for i in contours:
    accuracy = 0.01 * cv2.arcLength(i,True)
    approx = cv2.approxPolyDP(i,accuracy,True)
    # cv2.drawContours(image,[approx],-1,(0,255,0),2)
    if len(approx)<=3:
        name = "Triangle"
        cv2.drawContours(image,[i],0,(0,255,0),-1)
        M = cv2.moments(i)
        cx = int(M['m10']/M['m00'])
        cy = int(M['m01']/M['m00'])
        cv2.putText(image,name,(cx-60,cy),cv2.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)

cv2.imshow("Approx",image)
cv2.waitKey()


cv2.destroyAllWindows()