'''
  Contours
'''
import cv2 as cv
import numpy as np

img = cv.imread('Sample/f6797777cdb57641f748544e7140bfd8.jpg')
img = cv.resize(img, (3*img.shape[1]//4,3*img.shape[0]//4), interpolation=cv.INTER_CUBIC)
cv.imshow('Butterfly', img)

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grey', grey)

blur = cv.GaussianBlur(grey, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# hierrachies return contours hierarchies
# cv.RETR_LIST hierrachies mode is which contours are returned
# cv.RETR_EXTERNAL returns only external contours
# cv.RETR_TREE returns contours in hierarchical order

contours, hierrachies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')

ret, thresh = cv.threshold(grey, 150, 255, cv.THRESH_BINARY)
contours, hierrachies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
cv.imshow('Thresh', thresh)

print(f'{len(contours)} contours found!')

# ---------------------------------------------

canny = cv.Canny(img, 125, 175)
contours, hierrachies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

cv.imshow('Thresh_', canny)

print(f'{len(contours)} contours found!')

blank = np.zeros(img.shape, dtype = 'uint8')
cv.imshow('Blank', blank)

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours', blank)

print(f'{len(contours)} contours found!')

cv.waitKey(15000)
cv.destroyAllWindows()
