import cv2
import numpy as np

img = cv2.imread('images/image05.jpg',0)
img = cv2.medianBlur(img,7)

th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,11,2)

th2 = cv2.medianBlur(th2,7)

cv2.imshow('Input', img)
cv2.imshow('Output', th2)
#cv2.imwrite('images/image04_gs.jpg',th2)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()