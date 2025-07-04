import cv2 as cv

bq = cv.imread('Sample/FB_IMG_1473499987377.jpg')
cv.imshow('Bouque', bq)

grey = cv.cvtColor(bq, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', grey)

# Simple Thresholding
threshold, thresh = cv.threshold(grey, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple_threshold', thresh)

threshold, thresh_inv = cv.threshold(grey, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple_threshold_inverse', thresh_inv)

# Adaptive Thresholding
adap_thresh = cv.adaptiveThreshold(grey, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 7, 3)
cv.imshow('Adaptive Thresholding', adap_thresh)

cv.waitKey(5000)
cv.destroyAllWindows()
