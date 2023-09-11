#Import
from PIL import Image
from PIL import ImageEnhance
import matplotlib.pyplot as plt


im = Image.open(r"C:\Users\HP\Downloads\nature.JPG");

# Enhance Brightness
curr_bri = ImageEnhance.Brightness(im)
new_bri = 3
# Brightness enhanced by a factor of 2.5
img_brightened = curr_bri.enhance(new_bri)

# Enhance Color Level
curr_col = ImageEnhance.Color(img_brightened)
new_col = 1.5
img_colored = curr_col.enhance(new_col)

#Contrast
curr_con = ImageEnhance.Contrast(img_colored)
new_con = 1.5
  
# Contrast enhanced
img_contrasted = curr_con.enhance(new_con)
  
# shows updated image in image viewer
img_contrasted.show()  


#Plotting original
im_gray= im.convert('L')
#im_gray.show()  
hist=im_gray.histogram()
plt.figure(figsize=(12, 6))
#plt.hist(hist, bins=256, range=(0, 256), color='black', alpha=0.7)
plt.hist(range(256), bins=256, weights=hist[:256], color='gray',alpha=0.7)
plt.title('Histogram of Original Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.xlim(0, 256)  # Set the x-axis limit to the range of pixel values (0 to 256)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()

#Plotting original
im_gray2= img_contrasted.convert('L')
#im_gray.show()  
hist2=im_gray2.histogram()
plt.figure(figsize=(12, 6))
#plt.hist(hist, bins=256, range=(0, 256), color='black', alpha=0.7)
plt.hist(range(256), bins=256, weights=hist2[:256], color='black',alpha=0.7)
plt.title('Histogram of Revised Image')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.xlim(0, 256)  # Set the x-axis limit to the range of pixel values (0 to 256)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.show()