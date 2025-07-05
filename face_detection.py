'''
  Face detection
  on images
'''
import cv2 as cv

pic = cv.imread('Sample/pari.jpg')
# cv.imshow('Person',pic)

grey = cv.cvtColor(pic, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray_person',grey)

haar_cascade = cv.CascadeClassifier('data/haarcascade_frontalface_default.xml')
faces_rect = haar_cascade.detectMultiScale(grey,scaleFactor=1.1, minNeighbors=1)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(pic, (x,y), (x+w,y+w), (0, 255, 0), thickness=2)

cv.imshow('Detected Faces', pic)

cv.waitKey(5000)
cv.destroyAllWindows()
