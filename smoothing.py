'''
  Texture manupulation
'''
import cv2 as cv
import numpy as np

img = cv.imread('Sample/b17e876d5645ac617429b644a8b9c809.jpg')
img = cv.resize(img, (img.shape[1]//2, img.shape[0]//2), interpolation=cv.INTER_CUBIC)
cv.imshow('Trees',img)

kernel = np.ones((3,3), np.uint8)

# Averaging
average = cv.blur(img,(5,5))
cv.imshow('Average blur', average)

# Gaussian blur
gauss = cv.GaussianBlur(img, (5,5), 0)
cv.imshow("Gaussian blur", gauss)

# Medain blur
median = cv.medianBlur(img, 5)
cv.imshow("Medain blur", median)

# Bilateral blur
# sigma space = far pixel can influence space
# sigma color = more colors can influence blur
bilateral = cv.bilateralFilter(img, 5, 55, 55)
cv.imshow("Bilateral blur", bilateral)

cv.waitKey(15000)
cv.destroyAllWindows()
