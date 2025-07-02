"""Begin with opencv"""
import cv2 as cv
img = cv.imread('Sample/51ae5498806de05c32db478069a249a7.jpg')

cv.imshow('Picture',img)
cv.waitKey(2000)
cv.destroyAllWindows()
