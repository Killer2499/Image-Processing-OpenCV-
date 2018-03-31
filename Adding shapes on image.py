import numpy as np
import cv2

img=cv2.imread('goku.png',cv2.IMREAD_COLOR)#Reading the image

cv2.line(img,(0,0),(150,150),(255,255,255),15)#Draw a ling on the image
cv2.rectangle(img,(15,25),(200,150),(0,255,0),5)#Draw a rectangle on the image
cv2.circle(img,(100,63),55,(0,0,255),-1)#Draw Circle

pts = np.array([[10,5],[20,30],[70,20],[50,10]],np.int32)
#pts = pts.reshape((-1,1,2))
cv2.polylines(img,[pts],True,(0,255,255),3)

font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'Open Cv!!!',(0,130),font,1,(200,255,255),2,cv2.LINE_AA)
cv2.imshow('image',img)#Display the changed image
cv2.waitKey(0)
cv2.destroyAllWindows()