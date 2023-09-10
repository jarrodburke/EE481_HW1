import cv2
import numpy as np
import matplotlib.pyplot as plt

img0 = cv2.imread('Lenna.png', cv2.IMREAD_GRAYSCALE) #convert image greyscale

cv2.imshow('greyscale level 0',img0)    #display image level 0
img1 = cv2.pyrDown(img0)                #downscale image one level
cv2.imshow('greyscale level 1',img1)    #display image level 1
img2 = cv2.pyrDown(img1)                #downscale image one level
cv2.imshow('greyscale level 2',img2)    #display image level 2
img3 = cv2.pyrDown(img2)                #downscale image one level
cv2.imshow('greyscale level 3',img3)    #display image level 3

cv2.waitKey(0)
cv2.destroyAllWindows()