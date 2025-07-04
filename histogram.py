'''
  Histogram for the images
'''
import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

heart = cv.imread('Sample/FB_IMG_1454317100331.jpg')
cv.imshow('Heart',heart)

grey = cv.cvtColor(heart, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', grey)

blank = np.zeros(heart.shape[:2], dtype='uint8')
circle = cv.circle(blank, (heart.shape[1]//2, heart.shape[0]//2), 100, (255,), -1)
mask = cv.bitwise_and(grey, grey, mask=circle)
cv.imshow('Mask', mask)

# # Greyscale histogram
# grey_hist = cv.calcHist([grey], [0], None, [256], [0,256])

# plt.figure()
# plt.title('Greyscale histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(grey_hist)
# plt.xlim([0,256])
# plt.show()

# # Greyscale histogram with mask
# grey_hist = cv.calcHist([grey], [0], mask, [256], [0,256])

# plt.figure()
# plt.title('Greyscale histogram')
# plt.xlabel('Bins')
# plt.ylabel('# of pixels')
# plt.plot(grey_hist)
# plt.xlim([0,256])
# plt.show()

# Colour histogram
colour_mask = cv.bitwise_and(heart, heart, mask=circle)
cv.imshow('Colour masked',colour_mask)

plt.figure()
plt.title('Colour histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
for i,col in enumerate(('b','g','r')):
    hist = cv.calcHist([heart], [i], circle, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(2000)
cv.destroyAllWindows()
