import cv2
import numpy as np

image = cv2.imread(r"E:\Rishil's Documents\Python Programs 3\Computer Vision(Drishti Project)\Mastering OpenCV in Python(Udemy)\Master OpenCV\images\blobs.jpg",0)

cv2.imshow("Original image",image)
cv2.waitKey()


params = cv2.SimpleBlobDetector_Params()

params.filterByCircularity = True
params.minCircularity = 0.9

detector = cv2.SimpleBlobDetector_create(params)

keypoints = detector.detect(image)

blank = np.zeros((1,1))
blob = cv2.drawKeypoints(image,keypoints,blank,(0,255,255),cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

cv2.imshow("Blobs",blob)
cv2.waitKey()

cv2.destroyAllWindows()