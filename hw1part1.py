from PIL import Image, ImageOps
import matplotlib.pyplot as plt
myImage = Image.open("Winter.png")
myImage.show()

grayImage = ImageOps.grayscale(myImage)
grayImage.show()

histogram = grayImage.histogram()

plt.figure(figsize=(8, 6))
plt.hist(histogram, bins=256, range=(0, 256), color='gray', alpha=0.7)
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.title('Grayscale Histogram')
plt.xlim(0, 256)  # Set the x-axis limit to the range of pixel values (0 to 256)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Show the histogram
plt.show()
