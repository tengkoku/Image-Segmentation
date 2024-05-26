""" 
1. medianBlur (#recommended value = 3 or 5, higher mask for image with shadow or dim = 7 or 9)
2. adaptive gaussian threshold
3. medianBlur (#recommended value = 3 or 5, higher mask for image with shadow or dim = 7 or 9)
4. erosion

*gaussian adaptive
- small problem in image03, image 04
- gapping lines in the words but still readable
"""
import cv2
import numpy as np
from tkinter import filedialog
import tkinter as tk

def getImage():
    file = filedialog.askopenfilename()
    if file:
        return cv2.imread(file, 0)
    return None

def process_image(mask_size):
    img = getImage()
    if img is not None:
        img1 = cv2.medianBlur(img, mask_size) #Smoothen before segmentation
        th2 = cv2.adaptiveThreshold(img1, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2) # Gaussian Adaptive 
        th2 = cv2.medianBlur(th2, mask_size) #Smoothen before segmentation
        kernel = np.ones((2, 2), np.uint8) # Define the kernel size
        erosion = cv2.erode(th2, kernel, iterations = 1) # Perform erosion
        cv2.imshow('Input', img)
        cv2.imshow('Output', erosion)
        return erosion
    
    # Wait for a key press and then close the windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def set_mask_size():
    mask_size = int(spinbox.get())
    global output_image
    output_image = process_image(mask_size)

def save_image():
    file = filedialog.asksaveasfilename(defaultextension=".jpg")
    if file:
        cv2.imwrite(file, output_image)

# Create a tkinter window
window = tk.Tk()

mask_size_label = tk.Label(window, text="Mask Size:")
mask_size_label.pack()
spinbox = tk.Spinbox(window, from_=3, increment=2 ,to=9)
spinbox.pack()

process_button = tk.Button(window, text="Process Image", command=set_mask_size)
process_button.pack()

save_button = tk.Button(window, text="Save Image", command=save_image)
save_button.pack()

window.mainloop()

