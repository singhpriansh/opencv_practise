"""Reading image as cv"""
import cv2 as cv

img =  cv.imread("Sample/FB_IMG_1463724795912.jpg")
cv.imshow('Rose', img)
cv.waitKey(0)
