'''
  Colour convertions only
'''
import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Sample/edf4ce4e2ad199569ce9b8cd777fe299.jpg')
cv.imshow('Boston', img)

# # BGR to Grayscale
# grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Grey_', grey)

# # BGR to HSV
# hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('HSV', hsv)

# # BGR to LAB
# lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('Lab', lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

# RGB to BGR
bgr = cv.cvtColor(rgb, cv.COLOR_RGB2BGR)
cv.imshow("BGR", bgr)

# ----------------------------------------------

plt.imshow(rgb)
plt.show()

cv.waitKey(5000)
cv.destroyAllWindows()
