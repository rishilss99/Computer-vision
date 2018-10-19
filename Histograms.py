import cv2
import numpy
from matplotlib import pyplot as plt

image = cv2.imread("E:\Rishil's Documents\Python Programs 3\Computer Vision(Drishti Project)\Mastering OpenCV in Python(Udemy)\Master OpenCV\images\input.jpg")
# histogram = cv2.calcHist([image],[0],None,[256],[0,256]) #Just histogram is made but not displayed as to displayt it you need to use plt.plt(histogram,color='b')
# plt.hist(image.ravel(),256,[0,256])

color = ('b','g','r')
for i,col in enumerate(color):
    histogram = cv2.calcHist([image],[i],None,[256],[0,256])
    plt.plot(histogram,color=col)
    plt.xlim([0,256])
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()