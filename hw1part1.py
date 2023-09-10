import cv2
import matplotlib.pyplot as plt
import numpy as np

image_path = "Winter.png"
image = cv2.imread(image_path)



norm_image = cv2.normalize(image,None, 0, 255, cv2.NORM_MINMAX)

norm_image_bw = cv2.cvtColor(norm_image,cv2.COLOR_BGR2GRAY)

cv2.imshow("norm_image_color", norm_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imshow("norm_image_bw", norm_image_bw)

cv2.waitKey(0)
cv2.destroyAllWindows()




plt.figure(figsize=(8, 6))
plt.hist(norm_image_bw.ravel(), bins=256, range=(0, 256), color='black', alpha=0.7)
plt.title('Histogram of Normalized Image (Black and White)')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.xlim(0, 256)  
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

crop_img = norm_image_bw[400:500, 400:500]
cv2.imshow("crop", crop_img)
cv2.waitKey(0)



plt.figure(figsize=(8, 6))
plt.hist(crop_img.ravel(), bins=256, range=(0, 256), color='black', alpha=0.7)
plt.title('Histogram of Normalized Image (Black and White)')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.xlim(0, 256) 
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

plt.figure(figsize=(8, 6))
plt.hist(norm_image_bw.ravel(), bins=256, range=(0, 256), color='black', alpha=0.5, label='Grayscale Image')
plt.hist(crop_img.ravel(), bins=256, range=(0, 256), color='red', alpha=0.5, label='Cropped Region')
plt.title('Histograms of Grayscale Image and Cropped Region')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.xlim(0, 256)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.legend()
plt.show()