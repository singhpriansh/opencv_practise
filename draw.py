"""
Generation of Text and Shapes
"""
import cv2 as cv
import numpy as np

# img = cv.imread('Sample/2462f9dea7a0fbba219867388b864b75.jpg')
# cv.imshow('Random', img)

blank = np.zeros((500, 500, 3), dtype = 'uint8')
# cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
blank[:] = 200,100,100
# cv.imshow('Colour', blank)
blank[200:300, 300:400] = 0, 0, 255
# cv.imshow('Shape', blank)

# 2. Draw a rectangle
cv.rectangle(blank, (0,0), (500,250), (0,255,0), thickness=2)
# cv.imshow('Horizontal_rectangle', blank)
cv.rectangle(blank, (0,0), (250,500), (255,0,0), thickness=-1)
# cv.imshow('Vetical_rectangle', blank)
cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,255), thickness=-1)
# cv.imshow('Square', blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), blank.shape[1]//4, (0,0,255), thickness=3)
# cv.imshow('Circle_line', blank)
cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2),
          blank.shape[1]//6, (255,50,50), thickness=-1)
# cv.imshow('Circle_line', blank)

# 4.Draw a Line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=2)
# cv.imshow("Line",blank)
cv.line(blank, (blank.shape[1]//2,0),
        (blank.shape[1]//2, blank.shape[0]//2), (0,0,255), thickness=2)
# cv.imshow("Red_Line",blank)

# 5. Write Text
cv.putText(blank, 'Priyanshu', (10,80), cv.FONT_HERSHEY_TRIPLEX, 2.0, (200, 200, 255), 1)
# cv.imshow("Text", blank)

cv.imshow("Final", blank)
cv.waitKey(5000)
cv.destroyAllWindows()
