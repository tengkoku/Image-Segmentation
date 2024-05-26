import cv2
import numpy as np

# Load an image
img = cv2.imread('images/image01_gs.jpg', 0)

# Define the kernel size
kernel = np.ones((2,2),np.uint8)

# Perform dilation
dilation = cv2.dilate(img, kernel, iterations = 1)

# Display the original and dilated images
cv2.imshow('Original', img)
cv2.imshow('Dilation', dilation)

# Wait for a key press and then close the windows
cv2.waitKey(0)
cv2.destroyAllWindows()