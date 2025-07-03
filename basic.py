'''
  opnCV functions
'''
import cv2 as cv
import numpy as np

img = cv.imread("Sample/399d9b57dd7c10fbcf069a2e2d714df4.jpg")
cv.imshow('Autumn',img)

# Convering to greyscale
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Grey',grey)

# Blur
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# Edge Cascade
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# Dilated the image
kernel = np.ones((3,3), np.uint8)
dilated = cv.dilate(canny, kernel, iterations=1)
cv.imshow('Dilated', dilated)

# Eroding the image
eroded = cv.erode(dilated, kernel, iterations=1)
cv.imshow('Eroded',eroded)

# Resizing the image
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping the image
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(8000)
cv.destroyAllWindows()
