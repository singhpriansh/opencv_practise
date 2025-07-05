'''
  Faces train
'''
import os
import cv2 as cv
import numpy as np

people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
haar_cascade = cv.CascadeClassifier('data/haarcascade_frontalface_default.xml')

features = []
labels = []

def create_train():
    '''
      Training a model
    '''
    for person in people:
        path = 'Sample/Faces/train' + '/' + person
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)

            img_array = cv.imread(img_path)
            # grey = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(img_array, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi = img_array[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()

print('Trainging done ----------')
print(f'Length of the features = {len(features)}')
print(f'Length of the labels = {len(labels)}')

features = np.array(features, dtype='object')
labels = np.array(labels)

# face_recognizer = cv.face.LBPHFaceRecognizer_create()

# Train the recognizer on the features list and the labels list
# face_recognizer.train(features, labels)

face_recognizer.train(features, labels)
face_recognizer.save('face_trained.yml')
np.save('features.py',features)
np.save('labels.py',labels)
