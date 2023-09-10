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

hist = cv2.calcHist([norm_image_bw], [0], None, [256], [0, 256])

# Normalize the histogram

# Plot the histogram in black and white
plt.figure(figsize=(8, 6))
plt.hist(norm_image_bw.ravel(), bins=256, range=(0, 256), color='black', alpha=0.7)
plt.title('Histogram of Normalized Image (Black and White)')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.xlim(0, 256)  # Set the x-axis limit to the range of pixel values (0 to 256)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()


cv2.imshow(norm_image)
