'''
  Face recognition
'''
import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('data/haarcascade_frontalface_default.xml')

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
# features = np.load('features.npy')
# labels = np.load('labels.npy')

# face_recognizer = cv.face.LBPHFaceRecognizer_Create()
# face_recognizer.read('face_trained.yml')

img = cv.imread(r'Sample/Faces/val/ben_afflek/1.jpg')
cv.imshow('Person',img)

# Detect the face in the image
faces_rect = haar_cascade.detectMultiScale(img, 1.1, 4)

for (x,y,w,h) in faces_rect:
    faces_roi = img[y:y+h,x:x+h]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'Label = {label} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX,
               1.0, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)


cv.imshow('Detected face',img)
