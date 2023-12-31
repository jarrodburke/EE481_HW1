import cv2
import matplotlib.pyplot as plt

img = cv2.imread('valley.tif', cv2.IMREAD_GRAYSCALE)

eq_im = cv2.equalizeHist(img)
hist_or = cv2.calcHist([img], [0], None, [256], [0,256])
hist_eq = cv2.calcHist([eq_im],[0],None, [256], [0,256])

plt.figure(figsize=(12, 6))

plt.subplot(121)
plt.title('Original Image')
plt.plot(hist_or, color='black')
plt.xlim([0,256])
plt.grid()

plt.subplot(122)
plt.title('Equalized Image')
plt.plot(hist_eq, color='black')
plt.xlim([0,256])
plt.grid()

plt.tight_layout()
plt.show()

cv2.imshow('Original', img)
cv2.imshow('Equalized', eq_im)
cv2.waitKey(0)
cv2.destroyAllWindows()