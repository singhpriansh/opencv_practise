'''
  Masking in opencv
'''
import cv2 as cv
import numpy as np

cake = cv.imread('Sample/Birthday_Cake_2_Kg_Chocolate_PRCAKE140_b5e58052.jpg')
cv.imshow('Cake', cake)

blank = np.zeros(cake.shape[:2] ,dtype='uint8')
cake_center = (cake.shape[1]//2,cake.shape[0]//2)

mask = cv.circle(blank.copy(), cake_center, 120, (255,), -1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(cake, cake,mask=mask)
cv.imshow('Peek Cake', masked)

# ----------------Wierd shape-----------------
initial = (cake.shape[1]//2 - 100, cake.shape[1]//2 - 100)
final = (cake.shape[0]//2 + 100, cake.shape[0]//2 + 100)

rectangle = cv.rectangle(blank.copy(), initial, final, (255,), -1)
weird_shape = cv.bitwise_or(mask,rectangle)
cv.imshow("Weird_shape",cv.bitwise_and(cake,cake,mask=weird_shape))

cv.waitKey(10000)
cv.destroyAllWindows()
