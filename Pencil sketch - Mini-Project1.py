import cv2
import numpy as np

def sketch(image):
    """Use this function to make a sketch of the camera feed"""
    #First convert to greyscale
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

    #Blur to remove any noise
    blurred = cv2.medianBlur(gray,5)

    #Apply edge detection to give a sketch like effect
    canny = cv2.Canny(blurred,10,45)

    #Apply thresholding to revert the colors
    thresh,mask = cv2.threshold(canny,127,255,cv2.THRESH_BINARY_INV)

    return mask


cap = cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()
    cv2.imshow("Camera feed",sketch(frame))
    if cv2.waitKey(1)==13:
        break

cap.release()
cv2.destroyAllWindows()