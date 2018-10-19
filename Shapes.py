import numpy as np
import cv2

image = np.zeros([500,500,3],np.uint8) #Created a rectangle
#cv2.line(image,(0,0),(500,500),(125,256,0),5) #Diagonal across the rectangle
#cv2.circle(image,(200,200),50,(120,40,32),-1)
pts = np.array([[200,67],[11,1],[490,450],[0,16]])
pts = pts.reshape((-1,1,2))
cv2.polylines(image,[pts],True,(125,100,68),5)
cv2.putText(image,'Hello',(160,200),cv2.FONT_HERSHEY_COMPLEX,3,(124,0,6),5)

cv2.imshow("Polygon",image)
cv2.waitKey()
cv2.destroyAllWindows()