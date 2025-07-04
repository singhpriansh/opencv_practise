'''
  Gradients colors
'''
import cv2 as cv
import numpy as np

img = cv.imread('Sample/e1d8cf732c92e6b6846b945af1ebbebd.jpg')
cv.imshow('Design',img)

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', grey)

# Laplacian
lap = cv.Laplacian(grey, cv.CV_64F)
lap = np.absolute(lap)
lap = np.clip(lap, 0, 255).astype(np.uint8)
cv.imshow('Laplacian', lap)

# Sabel
sobelx = cv.Sobel(grey, cv.CV_64F, 1, 0)
sobely = cv.Sobel(grey, cv.CV_64F, 0, 1)
combine_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Sobel_combined', combine_sobel)

# ---- Canny edge detector
canny = cv.Canny(grey, 150, 175)
cv.imshow('Canny', canny)

cv.waitKey(5000)
cv.destroyAllWindows()
