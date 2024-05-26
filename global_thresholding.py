import cv2
import numpy as np

img = cv2.imread('images/image01.jpg',0) #coin_noise1.png
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,100,255,cv2.THRESH_BINARY)

#cv2.imshow('Original', img)
cv2.imshow('Thresh1', thresh1)
cv2.imshow('Thresh2', thresh2)
#cv2.imwrite('images/image01_gs.jpg',thresh2)

cv2.waitKey(0)
cv2.destroyAllWindows()
